from django.urls import path

from apps.mapping.views import CountryListAPIView, CountryRetrieveAPIView

app_name = 'mapping'
urlpatterns = [
    path('country/classifier/', CountryListAPIView.as_view(), name='country_list'),
    path('country/list/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryRetrieveAPIView.as_view(), name='country_retrieve'),
]
