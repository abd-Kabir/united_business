from django.contrib import admin

from apps.payment.models import Transaction, Subscription, Access

admin.site.register(Transaction)
admin.site.register(Subscription)
admin.site.register(Access)
