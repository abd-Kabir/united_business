from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True)
    phone_number = models.CharField(_("phone number"), max_length=19, blank=True)

    class Meta:
        db_table = 'User'
