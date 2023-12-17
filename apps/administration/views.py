from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from apps.administration.models import AboutUs, Direction, Partner
from apps.administration.serializer import AboutUsSerializer, DirectionSerializer, PartnerSerializer


class AboutUsModelViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    parser_classes = (MultiPartParser,)


class DirectionModelViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    parser_classes = (MultiPartParser,)


class PartnerModelViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    parser_classes = (MultiPartParser,)
