from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import BaseModel
from config.utils.api_exceptions import APIValidation


class VerifyCode(BaseModel):
    code = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'VerifyToken'


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(_("email address"), blank=True)
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True, null=True)
    phone_number = models.CharField(_("phone number"), max_length=19, blank=True, null=True)

    def save(self, *args, **kwargs):
        user = User.objects.filter(email=self.email, is_active=True)
        if user:
            raise APIValidation("This email is already registered")

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'User'
