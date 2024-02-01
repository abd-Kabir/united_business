from rest_framework.routers import DefaultRouter

from apps.administration.views import AboutUsModelViewSet, DirectionModelViewSet, PartnerModelViewSet, \
    ServiceModelViewSet, BannerModelViewSet, GuideModelViewSet

app_name = 'administration'
router = DefaultRouter()
router.register(r'about-us', AboutUsModelViewSet, basename='about_us')
router.register(r'direction', DirectionModelViewSet, basename='direction')
router.register(r'partner', PartnerModelViewSet, basename='partner')
router.register(r'service', ServiceModelViewSet, basename='service')
router.register(r'banner', BannerModelViewSet, basename='banner')
router.register(r'guide', GuideModelViewSet, basename='guide')

urlpatterns = router.urls
