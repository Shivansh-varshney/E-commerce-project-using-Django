from django.contrib import admin
from .models import User, CustomerAddress

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email',
                    'phone', 'first_name', 'last_name']


@admin.register(CustomerAddress)
class customerAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'addressname', 'housenumber', 'landmark',
                    'street', 'city', 'district', 'state', 'country', 'zipcode', 'status']
