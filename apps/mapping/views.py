from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.mapping.models import Country, Region, District
from apps.mapping.serializer import LocationSerializer, CountryClassifierSerializer, DistrictClassifierSerializer, \
    RegionClassifierSerializer


class CountryClassifierAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryClassifierSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = LocationSerializer


class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = LocationSerializer


class RegionClassifierListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionClassifierSerializer


class DistrictClassifierListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictClassifierSerializer

    def get_queryset(self):
        return District.objects.filter(region_id=self.kwargs['region'])
