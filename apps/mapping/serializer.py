from apps.mapping.models import Country

from rest_framework.fields import SerializerMethodField
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer


class LocationSerializer(GeoFeatureModelSerializer):
    test = SerializerMethodField()

    # def get_test(self, obj):
    #     return 'test'

    class Meta:
        model = Country
        geo_field = "geometry"
        fields = ('id', 'code', 'name', 'test')

    # def get_properties(self, instance, fields):
    #     return {
    #         'name': instance.name,
    #         'code': instance.code
    #     }
