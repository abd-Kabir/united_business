from django.urls import path

from apps.trade.views import TradeRepublicDataAPIView

app_name = 'trade'
urlpatterns = [
    path('republic-data/', TradeRepublicDataAPIView.as_view(), name='republic_data'),
]
