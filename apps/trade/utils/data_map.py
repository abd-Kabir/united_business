from django.core.cache import cache
from django.db.models import Sum, Max
from rest_framework import status

from apps.trade.models import Trade
from config.utils.api_exceptions import APIValidation


def trade_max(product, year):
    if not (product and year):
        raise APIValidation("No filters", status_code=status.HTTP_400_BAD_REQUEST)
    data_export = (
        Trade.objects
        .only('weight', 'price', 'date', 'product')
        .filter(TNVED=product, date__year=year, mode='ЭК')
        .values('country')
        .annotate(total_sum=Sum('price'))
        .aggregate(price=Max('total_sum'))
    )
    data_import = (
        Trade.objects
        .only('weight', 'price', 'date', 'product')
        .filter(TNVED=product, date__year=year, mode='ИМ')
        .values('country')
        .annotate(total_sum=Sum('price'))
        .aggregate(price=Max('total_sum'))
    )
    result = {
        "max_export": data_export['price'],
        "max_import": data_import['price']
    }
    return result


def trade_percent_max_min(max_import_value, max_export_value, export_compare, import_compare):
    if max_export_value:
        export_percent = round(((export_compare or 0) / max_export_value) * 100, 1)
    else:
        export_percent = 0
    if max_import_value:
        import_percent = round(((import_compare or 0) / max_import_value) * 100, 1)
    else:
        import_percent = 0
    return {
        "export_price_percent": export_percent,
        "import_price_percent": import_percent
    }
