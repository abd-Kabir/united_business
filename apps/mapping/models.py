from django.contrib.gis.db import models

from config.models import BaseModel


class Country(BaseModel):
    name = models.CharField('country name', max_length=255)
    code = models.CharField('country code', max_length=5)
    trade_name = models.CharField('trade name', max_length=255, null=True, blank=True, unique=True)
    geometry = models.GeometryField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Country'


class Region(BaseModel):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'Region'


class District(BaseModel):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'District'
