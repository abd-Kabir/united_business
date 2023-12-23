from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from apps.administration.models import AboutUs, Direction, Partner, Service
from apps.administration.serializer import AboutUsSerializer, DirectionSerializer, PartnerSerializer, ServiceSerializer
# from config.pagination import APIPagination
from config.utils.permissions import LandingPage


class AboutUsModelViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [LandingPage, ]
#     pagination_class = APIPagination


class ServiceModelViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [LandingPage, ]
#     pagination_class = APIPagination


class DirectionModelViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [LandingPage, ]
#     pagination_class = APIPagination


class PartnerModelViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [LandingPage, ]
#     pagination_class = APIPagination
