from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.trade.models import Trade
from apps.trade.serializer import TradeSerializer
from config.pagination import APIPagination


class TradeDataAPIView(ListAPIView):
    # def get(self, request):
    #     mode: str = request.query_params.get('mode')
    #     if mode.lower() == 'export':
    #         trade_queryset = Trade.objects.filter(mode="ЭК")
    #     else:
    #         trade_queryset = Trade.objects.filter(mode="ИМ")
    #     page = self.paginate_queryset(trade_queryset, request)
    #     return self.get_paginated_response(page)
    # queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    pagination_class = APIPagination

    def get_queryset(self):
        mode: str = self.request.query_params.get('mode')
        if mode.lower() == 'export':
            trade_queryset = Trade.objects.filter(mode="ЭК")
        else:
            trade_queryset = Trade.objects.filter(mode="ИМ")
        return trade_queryset
