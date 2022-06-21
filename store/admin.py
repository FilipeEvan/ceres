from django.contrib import admin
from .models import *

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt', 'state', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt', 'store')

