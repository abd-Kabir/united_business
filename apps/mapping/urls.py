from django.urls import path

from apps.mapping.views import CountryListAPIView

app_name = 'mapping'
urlpatterns = [
    path('country/list/', CountryListAPIView.as_view(), name='country_list')
]
