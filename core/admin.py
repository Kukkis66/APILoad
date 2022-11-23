from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Filemodel

admin.site.register(Filemodel)
admin.site.register(User, UserAdmin)

