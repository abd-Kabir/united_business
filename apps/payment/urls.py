from django.urls import path

from apps.payment.views import PaymeEndpointURL

urlpatterns = [
    path('merchant-api/', PaymeEndpointURL.as_view(), name='merchant-api'),
]
