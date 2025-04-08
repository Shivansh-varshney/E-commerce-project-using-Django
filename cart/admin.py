from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(CartOrder)
class cartorderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'txnid']


@admin.register(CartOrderItems)
class cartorderitemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price']
