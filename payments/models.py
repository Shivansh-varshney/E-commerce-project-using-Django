from userauths.models import User
from cart.models import CartOrder
from vendors.models import Vendor
from django.db import models

# Create your models here.


class transactions(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(
        CartOrder, on_delete=models.CASCADE, null=True, blank=True)
    txnid = models.CharField(max_length=255, null=True,
                             blank=True, unique=True)
    response_data = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.txnid


class payout_requests(models.Model):

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vendor.title

    class Meta:
        verbose_name_plural = 'Payout Requests'
