from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.mapping.models import Country
from apps.mapping.serializer import LocationSerializer, CountryClassifierSerializer


class CountryClassifierAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryClassifierSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = LocationSerializer


class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = LocationSerializer
