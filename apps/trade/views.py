from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.trade.models import Trade
from apps.trade.serializer import TradeSerializer
from config.pagination import APIPagination


class TradeDataAPIView(ListAPIView):
    queryset = Trade.objects.only('TNVED', 'product').distinct('TNVED').filter(product__isnull=False)
    serializer_class = TradeSerializer


class TradeRepublicDataAPIView(APIView):
    permission_classes = [AllowAny, ]

    # @method_decorator(cache_page(60 * 60 * 24))
    # @method_decorator(vary_on_cookie)
    def get(self, request):
        trade_import = Trade.objects.filter(mode='ИМ').only('weight', 'mode', 'product', 'date', 'price')
        trade_export = Trade.objects.filter(mode='ЭК').only('weight', 'mode', 'product', 'date', 'price')
        import_data_price_2023 = trade_import.filter(date__year=2023, product__isnull=False).aggregate(
            price_sum=Sum('price'))['price_sum']
        import_data_price_2022 = trade_import.filter(date__year=2022, product__isnull=False).aggregate(
            price_sum=Sum('price'))['price_sum']
        import_data_price_2021 = trade_import.filter(date__year=2021, product__isnull=False).aggregate(
            price_sum=Sum('price'))['price_sum']
        import_data_weight_2023 = trade_import.filter(date__year=2023, product__isnull=False).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        import_data_weight_2022 = trade_import.filter(date__year=2022, product__isnull=False).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        import_data_weight_2021 = trade_import.filter(date__year=2021, product__isnull=False).aggregate(
            weight_sum=Sum('weight'))['weight_sum']

        export_data_price_2023 = trade_export.filter(date__year=2023, product__isnull=False).aggregate(
            price_sum=Sum('price'))['price_sum']
        export_data_price_2022 = trade_export.filter(date__year=2022, product__isnull=False).aggregate(
            price_sum=Sum('price'))['price_sum']
        export_data_price_2021 = trade_export.filter(date__year=2021, product__isnull=False).aggregate(
            price_sum=Sum('price'))['price_sum']
        export_data_weight_2023 = trade_export.filter(date__year=2023, product__isnull=False).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        export_data_weight_2022 = trade_export.filter(date__year=2022, product__isnull=False).aggregate(
            weight_sum=Sum('weight'))['weight_sum']
        export_data_weight_2021 = trade_export.filter(date__year=2021, product__isnull=False).aggregate(
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
