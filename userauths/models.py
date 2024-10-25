from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class CustomerAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, unique=False)
    addressname = models.CharField(
        max_length=50, null=True, blank=True)
    housenumber = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    landmark = models.CharField(
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
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Customer Adresses"
