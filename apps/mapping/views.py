from rest_framework.generics import ListAPIView

from apps.mapping.models import Country
from apps.mapping.serializer import LocationSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = LocationSerializer
