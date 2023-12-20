from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.authentication.models import User, VerifyCode
from apps.authentication.serializers import JWTObtainPairSerializer, SignUpSerializer, SignUpAuthSerializer
from config.utils.api_exceptions import APIValidation


class JWTObtainPairView(TokenObtainPairView):
    serializer_class = JWTObtainPairSerializer
    permission_classes = [AllowAny, ]


class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"detail": "Continue registration", "user": user.email})


class SignUpVerifyCodeAPIView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        code = request.data.get('code')
        email = request.data.get('email')
        email_user = get_object_or_404(User, verifycode__code=code)
        # if email_user:
        #     email_users = list(email_user)
        #     email_user = email_users.pop(-1)
        # else:
        #     raise APIValidation("Code is incorrect", status_code=status.HTTP_400_BAD_REQUEST)

        verify_obj = VerifyCode.objects.filter(code=code)
        if verify_obj:
            verify_obj: VerifyCode = verify_obj.first()

            user = verify_obj.user
            if user == email_user:
                verify_obj.is_verified = True
                user.is_active = True
                user.save()
                verify_obj.save()

                User.objects.filter(email=email, is_active=False).delete()
                return Response({
                    'detail': 'Successfully verified',
                    'status': status.HTTP_200_OK
                })
        else:
            raise APIValidation("Code is incorrect", status_code=status.HTTP_400_BAD_REQUEST)


class SignUpAuthAPIView(APIView):
    def post(self, request):
        try:
            serializer = SignUpAuthSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh['username'] = user.username
            refresh['first_name'] = user.first_name
            refresh['last_name'] = user.last_name
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        except Exception as exc:
            raise APIValidation(f"Error occurred: {exc.args}")
