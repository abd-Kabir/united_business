from django.urls import path

from apps.payment.views import PaycomMerchantAPI

app_name = 'payment'
urlpatterns = [
    path('merchant-api/', PaycomMerchantAPI.as_view(), name='merchant-api'),
]
