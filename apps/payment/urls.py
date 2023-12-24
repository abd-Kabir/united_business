from django.urls import path

from apps.payment.views import PaymeEndpointURL

app_name = 'payment'
urlpatterns = [
    path('merchant-api/', PaymeEndpointURL.as_view(), name='merchant-api'),
]
