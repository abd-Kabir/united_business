from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.views import JWTObtainPairView, SignUpAPIView, SignUpVerifyCodeAPIView, SignUpAuthAPIView

urlpatterns = [
    path('token/', JWTObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # sign-up
    path('sign-up/', SignUpAPIView.as_view(), name='sign_up'),
    path('verify/', SignUpVerifyCodeAPIView.as_view(), name='verify'),
    path('sign-in/', SignUpAuthAPIView.as_view(), name='sign_in'),
]
