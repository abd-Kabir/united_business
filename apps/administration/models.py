from django.db import models

from apps.tools.utils.hash import hash_filename
from config.models import BaseModel


class AboutUs(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    # title_secondary = models.CharField(max_length=255, null=True, blank=True)
    # description_secondary = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    photo = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'AboutUs'


class Service(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    # title_secondary = models.CharField(max_length=255, null=True, blank=True)
    # description_secondary = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    photo = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'Service'


class Direction(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    # title_secondary = models.CharField(max_length=255, null=True, blank=True)
    # description_secondary = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    photo = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'Direction'


class Partner(BaseModel):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    description_uz = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    description_en = models.TextField(null=True)
    link = models.TextField(null=True, blank=True)
    logo = models.FileField(upload_to=hash_filename)
    photo = models.FileField(upload_to=hash_filename)

    class Meta:
        db_table = 'Partner'
