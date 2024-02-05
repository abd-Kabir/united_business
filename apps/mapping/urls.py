from django.urls import path

from apps.mapping.views import CountryListAPIView, CountryRetrieveAPIView, CountryClassifierAPIView, \
    RegionClassifierListAPIView, DistrictClassifierListAPIView

app_name = 'mapping'
urlpatterns = [
    path('country/classifier/', CountryClassifierAPIView.as_view(), name='country_classifier'),
    path('country/list/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryRetrieveAPIView.as_view(), name='country_retrieve'),
    path('regions/', RegionClassifierListAPIView.as_view(), name='regions'),
    path('districts/<int:region>/', DistrictClassifierListAPIView.as_view(), name='districts_by_region'),
]
