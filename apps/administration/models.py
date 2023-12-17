from django.db import models

from apps.tools.utils.hash import hash_filename
from config.models import BaseModel


class AboutUs(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    link = models.TextField(null=True)
    photo = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'AboutUs'


class Direction(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    link = models.TextField(null=True)
    photo = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'Direction'


class Partner(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    photo_1 = models.FileField(upload_to=hash_filename)
    photo_2 = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'Partner'
