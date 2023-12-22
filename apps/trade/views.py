from django.db.models import Sum
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.trade.models import Trade
from apps.trade.serializer import TradeSerializer
from config.pagination import APIPagination


class TradeDataAPIView(ListAPIView):
    serializer_class = TradeSerializer
    pagination_class = APIPagination

    def get_queryset(self):
        mode: str = self.request.query_params.get('mode')
        if mode.lower() == 'export':
            trade_queryset = Trade.objects.filter(mode="ЭК")
        else:
            trade_queryset = Trade.objects.filter(mode="ИМ")
        return trade_queryset


class TradeRepublicDataAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        import_data_price_2023 = Trade.objects.filter(mode='ИМ').filter(date__year=2023).aggregate(
            price_sum=Sum('price'))['price_sum']
        import_data_price_2022 = Trade.objects.filter(mode='ИМ').filter(date__year=2022).aggregate(
            price_sum=Sum('price'))['price_sum']
        import_data_price_2021 = Trade.objects.filter(mode='ИМ').filter(date__year=2021).aggregate(
            price_sum=Sum('price'))['price_sum']
        import_data_weight_2023 = Trade.objects.filter(mode='ИМ').filter(date__year=2023).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        import_data_weight_2022 = Trade.objects.filter(mode='ИМ').filter(date__year=2022).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        import_data_weight_2021 = Trade.objects.filter(mode='ИМ').filter(date__year=2021).aggregate(
            weight_sum=Sum('weight'))['weight_sum']

        export_data_price_2023 = Trade.objects.filter(mode='ЭК').filter(date__year=2023).aggregate(
            price_sum=Sum('price'))['price_sum']
        export_data_price_2022 = Trade.objects.filter(mode='ЭК').filter(date__year=2022).aggregate(
            price_sum=Sum('price'))['price_sum']
        export_data_price_2021 = Trade.objects.filter(mode='ЭК').filter(date__year=2021).aggregate(
            price_sum=Sum('price'))['price_sum']
        export_data_weight_2023 = Trade.objects.filter(mode='ЭК').filter(date__year=2023).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        export_data_weight_2022 = Trade.objects.filter(mode='ЭК').filter(date__year=2022).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        export_data_weight_2021 = Trade.objects.filter(mode='ЭК').filter(date__year=2021).aggregate(
            weight_sum=Sum('weight'))['weight_sum']

        return Response({
            "import": {
                "price_2023": import_data_price_2023,
                "price_2022": import_data_price_2022,
                "price_2021": import_data_price_2021,
                "weight_2023": import_data_weight_2023,
                "weight_2022": import_data_weight_2022,
                "weight_2021": import_data_weight_2021,
            },
            "export": {
                "price_2023": export_data_price_2023,
                "price_2022": export_data_price_2022,
                "price_2021": export_data_price_2021,
                "weight_2023": export_data_weight_2023,
                "weight_2022": export_data_weight_2022,
                "weight_2021": export_data_weight_2021,
            }
        })
