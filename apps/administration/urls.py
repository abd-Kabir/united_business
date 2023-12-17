from rest_framework.routers import DefaultRouter

from apps.administration.views import AboutUsModelViewSet, DirectionModelViewSet, PartnerModelViewSet

router = DefaultRouter()
router.register(r'about-us', AboutUsModelViewSet, basename='about_us')
router.register(r'direction', DirectionModelViewSet, basename='direction')
router.register(r'partner', PartnerModelViewSet, basename='partner')

urlpatterns = router.urls
