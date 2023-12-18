from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.authentication.models import User, VerifyCode
from apps.tools.utils.mailing import send_verification_token
from config.utils.api_exceptions import APIValidation


class JWTObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token


class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        try:
            first_name = validated_data.get('first_name')
            last_name = validated_data.get('last_name')
            email = validated_data.get('email')

            user = User.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       email=email,
                                       username=None,
                                       is_active=False)
            send_verification_token(user=user, template_name='verification.html', subject='Verification Code')
            return user
        except Exception as exc:
            raise APIValidation(f"Error occurred: {exc.args}")


class SignUpAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    code = serializers.CharField()

    def create(self, validated_data):
        try:
            code = validated_data.get('code')
            email = validated_data.get('email')
            password = validated_data.get('password')
            username = validated_data.get('username')

            if not User.objects.filter(verifycode__code=code, email=email):
                raise APIValidation("Bad request", status_code=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(verifycode__code=code)
            VerifyCode.objects.get(code=code).delete()
            user.username = username
            # user.is_active = True
            user.set_password(password)
            user.save()
            return user
        except Exception as exc:
            raise APIValidation(f"Error occurred: {exc.args}")
