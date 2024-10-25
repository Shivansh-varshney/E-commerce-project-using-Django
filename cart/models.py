from django.db import models
from core.models import Product
from userauths.models import User, CustomerAddress
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICE = {
    "Processing": "Processing",
    "Shipped": "Shipped",
    "Delivered": "Delivered",
}

# Create your models here.


class CartOrder(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    txnid = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, default='null')
    phone = models.CharField(null=True, blank=True,
                             unique=False, max_length=50)
    name = models.CharField(max_length=200, default='null')
    address = models.ForeignKey(
        CustomerAddress, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default='0.99')
    paid_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        choices=STATUS_CHOICE, max_length=20, default='processing')

    class Meta:
        verbose_name_plural = "Cart Orders"

    def __str__(self) -> str:
        return self.user.username


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default='0.99')
    total = models.DecimalField(
        max_digits=12, decimal_places=2, default='0.99')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cart Order Items"
