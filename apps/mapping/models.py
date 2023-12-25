from django.contrib.gis.db import models

from config.models import BaseModel


class Country(BaseModel):
    name = models.CharField('country name', max_length=255)
    code = models.CharField('country code', max_length=5)
    geometry = models.GeometryField()

    def __str__(self):
        return self.name

    @property
    def test(self):
        return 123

    class Meta:
        db_table = 'Country'
