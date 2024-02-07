from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.views import JWTObtainPairAccountView, SignUpAPIView, SignUpVerifyCodeAPIView, \
    SignUpAuthAPIView, JWTObtainPairManagementView, PersonalDataAPIView, PersonalDataRetrieveAPIView

app_name = 'auth'
urlpatterns = [
    path('account/token/', JWTObtainPairAccountView.as_view(), name='token_obtain_pair'),
    path('management/token/', JWTObtainPairManagementView.as_view(), name='management_token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # sign-up
    path('sign-up/', SignUpAPIView.as_view(), name='sign_up'),
    path('verify/', SignUpVerifyCodeAPIView.as_view(), name='verify'),
    path('sign-in/', SignUpAuthAPIView.as_view(), name='sign_in'),

    # personal-cabinet
    path('personal-data/<int:pk>/', PersonalDataAPIView.as_view(), name='personal_data_update'),
    path('personal-data/', PersonalDataRetrieveAPIView.as_view(), name='personal_data_retrieve'),
]
