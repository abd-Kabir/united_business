from django.urls import path

from apps.trade.views import TradeDataAPIView

app_name = 'trade'
urlpatterns = [
    path('', TradeDataAPIView.as_view(), name='trade'),
]
