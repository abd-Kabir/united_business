from django.db import models

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
