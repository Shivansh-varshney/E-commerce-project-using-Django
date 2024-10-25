from django.contrib import admin
from .models import vendor_review, Vendor, vendorAddress, vendorBankDetails, changeRequest

# Register your models here.


@admin.register(Vendor)
class vendorAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'vendor_image']


@admin.register(vendorAddress)
class vendoraddressAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'floornumber', 'building',
                    'street', 'city', 'district', 'state', 'country', 'zipcode']


@admin.register(vendorBankDetails)
class vendorbankdetailAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'bank_name', 'account_holder_name', 'account_number',
                    'account_type', 'ifsc', 'branch_address', 'pan_number', 'gst_number', 'cin']


@admin.register(vendor_review)
class vendorreviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'vendor']


@admin.register(changeRequest)
class changeRequest(admin.ModelAdmin):
    list_display = ['vendor', 'request_ticket', 'date', 'status']
