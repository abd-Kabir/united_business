from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from apps.trade.models import Trade
from apps.mapping.models import Country, District, Region
from apps.trade.utils.data_map import trade_max, trade_percent_max_min


class CountryClassifierSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')
    value = serializers.CharField(source='id')

    class Meta:
        model = Country
        fields = [
            'label',
            'value',
        ]


class RegionClassifierSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')
    value = serializers.CharField(source='id')

    class Meta:
        model = Region
        fields = [
            'label',
            'value',
        ]


class DistrictClassifierSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')
    value = serializers.CharField(source='id')

    class Meta:
        model = District
        fields = [
            'label',
            'value',
        ]


class LocationSerializer(GeoFeatureModelSerializer):
    trade_data = SerializerMethodField()

    def get_trade_data(self, obj):
        product = self.context.get('request').query_params.get('product')
        year = self.context.get('request').query_params.get('year')
        trade_name = obj.trade_name
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
        max_data = trade_max(product, year)
        percent = trade_percent_max_min(max_import_value=max_data['max_import'],
                                        max_export_value=max_data['max_export'],
                                        export_compare=data_export['price'],
                                        import_compare=data_import['price'])
        return {
            "export": {
                "price": data_export['price'],
                "weight": data_export['weight'],
                "percent": percent['export_price_percent'],
                "max": max_data['max_export']
            },
            "import": {
                "price": data_import['price'],
                "weight": data_import['weight'],
                "percent": percent['import_price_percent'],
                "max": max_data['max_import']
            }
        }

    class Meta:
        model = Country
        geo_field = "geometry"
        fields = ('id', 'code', 'name', 'trade_data')

    # def get_properties(self, instance, fields):
    #     return {
    #         'name': instance.name,
    #         'code': instance.code
    #     }
