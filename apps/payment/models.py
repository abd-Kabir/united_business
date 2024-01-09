from random import randint

from django.db import models

from config.models import BaseModel


class Subscription(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
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
    order_key = models.CharField(max_length=50, unique=True, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    perform_datetime = models.CharField(null=True, max_length=255)
    cancel_datetime = models.CharField(null=True, max_length=255)

    def __str__(self):
        return f"{self.order_key}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.payment_id:
            self.payment_id = randint(100_000, 999_999)
        # if not self.order_key:
        #     self.order_key = f"{uuid.uuid4().hex}-{int(time.time())}"
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'Transaction'
