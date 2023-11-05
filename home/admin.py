from django.contrib import admin

from .models import Product, Account
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# Register your models here.

admin.site.register(
    Account, UserAdmin
)

admin.site.register(Product)

# app_models = apps.get_app_config('home').get_models()
# for model in app_models:
#     try:    

#         admin.site.register(model)

#     except Exception:
#         pass
