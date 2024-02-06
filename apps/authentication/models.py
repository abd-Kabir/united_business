from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.mapping.models import Region, District
from apps.tools.utils.hash import hash_filename
from config.models import BaseModel
from config.utils.api_exceptions import APIValidation

username_validator = UnicodeUsernameValidator()


class VerifyCode(BaseModel):
    code = models.CharField(max_length=6, unique=True)
    is_verified = models.BooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=1, related_name='verifycode')

    class Meta:
        db_table = 'VerifyToken'


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True, blank=True
    )
    email = models.EmailField(_("email address"), blank=True)
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True, null=True)
    phone_number = models.CharField(_("phone number"), max_length=19, blank=True, null=True)

    NO_CHOICE = None
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (NO_CHOICE, "Tanlanmagan"),
        (MALE, "Erkak"),
        (FEMALE, "Ayol"),
    ]
    gender = models.CharField(_("gender"), max_length=6, choices=GENDER_CHOICES, default=NO_CHOICE,
                              null=True, blank=True)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    NO_CHOICE = None
    LEGAL = "LEGAL"
    PHYSICAL = "PHYSICAL"
    USER_TYPE_CHOICES = [
        (LEGAL, "Yuridik shaxs"),
        (PHYSICAL, "Jismoniy shaxs"),
    ]
    user_type = models.CharField(max_length=8, choices=USER_TYPE_CHOICES, default=NO_CHOICE,
                                 null=True, blank=True)
    company_name = models.CharField(_('company name'), max_length=255, null=True, blank=True)
    founded = models.DateField(_('founded in'), null=True, blank=True)
    company_description = models.TextField(_('company description'), null=True, blank=True)
    licence_file = models.FileField(_('licence file'), upload_to=hash_filename, null=True, blank=True)
    certificate_file = models.FileField(_('certificate file'), upload_to=hash_filename, null=True, blank=True)

    def save(self, *args, **kwargs):
        user = User.objects.filter(email=self.email, is_active=True)
        if user and (not self.pk):
            raise APIValidation("This email is already registered")

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'User'
