import uuid

from django.db import models

from apps.authentication.models import User
from config.models import BaseModel


class Subscription(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.FloatField()
    USD = 'USD'
    UZS = 'UZS'
    UNIT_CHOICES = [
        (USD, "Dollar"),
        (UZS, "So'm"),
    ]
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default=UZS)

    class Meta:
        db_table = 'Subscription'


class Access(BaseModel):
    name = models.CharField(max_length=255)
    subscription = models.ManyToManyField(Subscription, related_name='accesses')
    access_til = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Access'


class Transaction(BaseModel):
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILED = 'failed'
    CANCELED = 'canceled'
    STATUS = (
        (PROCESSING, 'processing'),
        (SUCCESS, 'success'),
        (FAILED, 'failed'),
        (CANCELED, 'canceled')
    )
    status = models.CharField(choices=STATUS, default='processing', max_length=55)
    payment_id = models.IntegerField(null=True, blank=True)
    transaction_key = models.CharField(max_length=255, null=True, blank=True)
    state = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    create_datetime = models.DateTimeField(null=True, blank=True)
    perform_datetime = models.DateTimeField(null=True, blank=True)
    cancel_datetime = models.DateTimeField(null=True, blank=True)
    reason = models.IntegerField(blank=True, null=True)

    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.payment_id}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.payment_id:
            self.payment_id = uuid.uuid4().hex
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'Transaction'
