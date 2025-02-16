from django.contrib import admin
from django.contrib.auth.models import User
from login.custom_admin import register_models_with_custom_admin

# Register your models here.

admin.site.unregister(User)
register_models_with_custom_admin()