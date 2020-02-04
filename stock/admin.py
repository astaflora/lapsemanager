from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'created_by', 'modified_by', 'created_at', 'modified_at', 'is_deleted')


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'store')


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'phone', 'store', 'created_by', 'modified_by',
                    'created_at', 'modified_at', 'is_deleted')


@admin.register(models.Message)
class Message(admin.ModelAdmin):
    list_display = ('pk', 'person', 'customer', 'object', 'message', 'date', 'created_by', 'modified_by', 'created_at',
                    'modified_at', 'is_deleted')


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ('pk', 'designation', 'date_ent_stock', 'date_peremption', 'stock_init', 'stock_dt', 'price_ini',
                    'price_promo', 'store', 'category', 'created_by', 'modified_by', 'created_at', 'modified_at',
                    'is_deleted')
