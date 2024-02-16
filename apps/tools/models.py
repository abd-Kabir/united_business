from django.db import models

from apps.mapping.models import District
from config.models import BaseModel


class Cluster(BaseModel):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    area = models.FloatField()

    class Meta:
        db_table = 'Cluster'


class SectorClassifier(BaseModel):
    mark = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    short_name = models.CharField(max_length=155, null=True, blank=True)
    tnved = models.CharField(max_length=50)

    class Meta:
        db_table = 'SectorClassifier'


class Certificate(BaseModel):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    stir = models.CharField(max_length=14, null=True, blank=True)
    industrial_networks = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    quality_systems = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'Certificate'
