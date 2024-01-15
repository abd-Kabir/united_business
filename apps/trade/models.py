from django.db import models

from apps.mapping.models import Country
from config.models import BaseModel


class Trade(BaseModel):
    mode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    TNVED = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    stir_pinfl = models.CharField(max_length=14, null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def country_rel_insert(self):
        self.country_rel_id = self.country
        self.save()

    class Meta:
        db_table = 'Trade'
        indexes = [
            models.Index(fields=['TNVED', 'date', 'country', 'mode', 'product']),
        ]
