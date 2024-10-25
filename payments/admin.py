from django.contrib import admin
from .models import transactions, payout_requests

# Register your models here.


@admin.register(transactions)
class transactionsAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'order', 'txnid']


@admin.register(payout_requests)
class payoutAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'amount', 'date']
