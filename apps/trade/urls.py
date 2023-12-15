from django.urls import path

from apps.trade.views import TradeDataAPIView

urlpatterns = [
    path('', TradeDataAPIView.as_view(), name='trade'),
]
