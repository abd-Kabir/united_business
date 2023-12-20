from django.contrib import admin

from apps.authentication.models import User, VerifyCode

admin.site.register(User)
admin.site.register(VerifyCode)
