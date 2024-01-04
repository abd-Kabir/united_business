# from datetime import datetime
#
# from rest_framework.fields import SerializerMethodField
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
#
# from apps.trade.utils.data_map import trade_map_data
# from apps.mapping.models import Country
#
#
# class LocationSerializer(GeoFeatureModelSerializer):
#     trade_data = SerializerMethodField()
#
#     def get_trade_data(self, obj):
#         start = datetime.now()
#         product = self.context.get('request').query_params.get('product')
#         year = self.context.get('request').query_params.get('year')
#         trade_name = obj.trade_name
#         trade_data = trade_map_data(product, year, trade_name)
#         end = datetime.now()
#         print("Time spent: ", end - start)
#         return trade_data
#
#     class Meta:
#         model = Country
#         geo_field = "geometry"
#         fields = ('id', 'code', 'name', 'trade_data')
#
#     # def get_properties(self, instance, fields):
#     #     return {
#     #         'name': instance.name,
#     #         'code': instance.code
#     #     }
