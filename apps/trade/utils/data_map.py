from django.db.models import Sum, IntegerField
from django.db.models.functions import Coalesce
from rest_framework import status

from apps.trade.models import Trade
from config.utils.api_exceptions import APIValidation


def trade_map_data(product, year, trade_name):
    if not (product and year):
        raise APIValidation("No filters", status_code=status.HTTP_400_BAD_REQUEST)
    data_export = (
        Trade.objects
        .only('weight', 'price', 'date', 'product')
        .filter(TNVED=product, date__year=year, country=trade_name, mode='ЭК')
        .aggregate(price=Sum('price'), weight=Sum('weight'))
    )
    data_import = (
        Trade.objects
        .only('weight', 'price', 'date', 'product')
        .filter(TNVED=product, date__year=year, country=trade_name, mode='ИМ')
        .aggregate(price=Sum('price'), weight=Sum('weight'))
    )

    return {
        "import": {
            "price": data_import.get('price'),
            "weight": data_import.get('weight')
        },
        "export": {
            "price": data_export.get('price'),
            "weight": data_export.get('weight')
        }
    }
