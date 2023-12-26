from django.urls import path

from apps.trade.views import TradeRepublicDataAPIView, TradeDataAPIView

app_name = 'trade'
urlpatterns = [
    path('products/', TradeDataAPIView.as_view(), name='products'),
    path('republic-data/', TradeRepublicDataAPIView.as_view(), name='republic_data'),
]
