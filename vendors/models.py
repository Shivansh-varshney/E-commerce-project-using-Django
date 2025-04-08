from django.db import models
from userauths.models import User
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
RATING = {
    1: "⭐✯✯✯✯",
    2: "⭐⭐✯✯✯",
    3: "⭐⭐⭐✯✯",
    4: "⭐⭐⭐⭐✯",
    5: "⭐⭐⭐⭐⭐",
}

ACCOUNT_TYPE = {
    'Savings Account': 'Savings Account',
    'Current Account': 'Current Account',
    'Personal Account': 'Personal Account',
    'Merchant Account': 'Merchant Account',
}

CHANGE_OPTION = {
    'Personal Details': 'Personal Details',
    'Bank Details': 'Bank Details',
    'Address': 'Address'
}

REQUEST_STATUS = {
    'Open': 'Open',
    'Closed': 'Closed',
    'Rejected': 'Rejected'
}


def user_directory_path(instance, filename):
    return f"user_{instance.user.id}/{filename}"


class Vendor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    vendor_id = ShortUUIDField(unique=True, length=10, max_length=20,
                               null=True, blank=True, prefix="vid", alphabet="abcdefghjklmnpqrstuvwxyx23456789")
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True)

    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50"')

    def __str__(self):
        return self.title


class vendorBankDetails(models.Model):

    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    bank_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    account_holder_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    account_number = models.IntegerField(unique=True, null=True, blank=True)
    account_type = models.CharField(
        choices=ACCOUNT_TYPE, max_length=60, null=True, blank=True)
    ifsc = models.CharField(max_length=50, null=True, blank=True)
    branch_address = models.CharField(max_length=400, null=True, blank=True)
    pan_number = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    gst_number = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    cin = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = 'Vendor Bank Details'


class vendorAddress(models.Model):
    vendor = models.OneToOneField(
        Vendor, on_delete=models.CASCADE, unique=False)
    floornumber = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    building = models.CharField(
        max_length=50, unique=False, null=True, blank=True)
    street = models.CharField(
        max_length=250, unique=False, null=True, blank=True)
    city = models.CharField(
        max_length=250, unique=False, null=True, blank=True)
    district = models.CharField(
        max_length=250, unique=False, null=True, blank=True)
    state = models.CharField(
        max_length=250, unique=False, null=True, blank=True)
    country = models.CharField(
        max_length=250, unique=False, null=True, blank=True)
    zipcode = models.IntegerField(unique=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Vendor Addresses'


class changeRequest(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    request_ticket = ShortUUIDField(unique=True, length=10, max_length=20,
                                    null=True, blank=True, prefix="REQ", alphabet="abcdefghjklmnpqrstuvwxyx23456789")
    change_field = models.CharField(choices=CHANGE_OPTION, max_length=50)
    reason = models.TextField(max_length=300)

    date = models.DateField(auto_now_add=True)

    status = models.CharField(choices=REQUEST_STATUS,
                              max_length=50, default='Open')

    class Meta:
        verbose_name_plural = 'Information Change Requests'


class vendor_review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(choices=RATING, default=5)

    class Meta:
        verbose_name_plural = 'Vendor Reviews'
