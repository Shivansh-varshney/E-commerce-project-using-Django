from django.db import models
from vendors.models import Vendor
from userauths.models import User
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from shortuuid.django_fields import ShortUUIDField
# Create your models here.


STATUS = {
    "Disabled": "Disabled",
    "Rejected": "Rejected",
    "In review": "In review",
    "Published": "Published",
}

RATING = {
    1: "⭐✯✯✯✯",
    2: "⭐⭐✯✯✯",
    3: "⭐⭐⭐✯✯",
    4: "⭐⭐⭐⭐✯",
    5: "⭐⭐⭐⭐⭐",
}

SIZES = {
    "XS": "XS",
    "S": "S",
    "M": "M",
    "L": "L",
    "XL": "XL",
    "XXL": "XXL",
    "XXXL": "XXXL",
    "390 x 844": "390 x 844",
    "414 x 896": "414 x 896",
    "375 x 812": "375 x 812",
    "414 x 896": "414 x 896",
    "375 x 812": "375 x 812",
    "414 x 736": "414 x 736",
    "375 x 667": "375 x 667",
    "414 x 736": "414 x 736",
    "375 x 667": "375 x 667",
    "414 x 736": "414 x 736",
    "375 x 667": "375 x 667",
    "320 x 568": "320 x 568",
    "320 x 568": "320 x 568",
    "768 x 1024": "768 x 1024",
    "768 x 1024": "768 x 1024",
    "768 x 1024": "768 x 1024",
    "768 x 1024": "768 x 1024",
    "1170 x 2532": "1170 x 2532",
    "828 x 1792	": "828 x 1792",
    "1125 x 2436": "1125 x 2436",
    "1242 x 2688": "1242 x 2688",
    "1125 x 2436": "1125 x 2436",
    "1080 x 1920": "1080 x 1920",
    "750 x 1334	": "750 x 1334",
    "1080 x 1920": "1080 x 1920",
    "750 x 1334	": "750 x 1334",
    "1080 x 1920": "1080 x 1920",
    "750 x 1334	": "750 x 1334",
    "640 x 1136	": "640 x 1136",
    "640 x 1136	": "640 x 1136",
    "2048 x 2732": "2048 x 2732",
    "1536 x 2048": "1536 x 2048",
    "1536 x 2048": "1536 x 2048",
    "1536 x 2048": "1536 x 2048",
    "768 x 1024":  "768 x 1024",
    "1024 x 1366": "1024 x 1366",
}

RETURN_OPTIONS = {
    "7 Days": "7 Days",
    "14 Days": "14 Days",
    "21 Days": "21 Days",
    "1 Month": "1 Month",
    "Not Available": "Not Available",
}


def user_directory_path(instance, filename):
    return f"user_{instance.vendor.id}/{filename}"


class Category(models.Model):

    cid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="cat", alphabet="abcdefghjklmnpqrstuvwxyx23456789")
    title = models.CharField(max_length=100)
    image = models.Imnull = models.ImageField(
        null=True, blank=True, upload_to='category')

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50"/>')

    def __str__(self):
        return self.title


class Product(models.Model):

    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="product")
    tags = TaggableManager(blank=True)

    pid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="prd", alphabet="abcdefghjklmnpqrstuvwxyx23456789")

    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,
                              upload_to=user_directory_path)
    price = models.DecimalField(
        max_digits=12, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    description = models.TextField(
        null=True, blank=True)
    specifications = models.TextField(null=True, blank=True)

    manufacturer = models.CharField(null=True, blank=True, max_length=200)
    manufactured = models.DateField(null=True, blank=True)
    expiring = models.DateField(null=True, blank=True)
    warranty_period = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(
        choices=SIZES, max_length=50, null=True, blank=True)
    return_options = models.CharField(
        choices=RETURN_OPTIONS, default="Not Available", max_length=30)
    assured = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    product_status = models.CharField(
        choices=STATUS, max_length=15)

    sku = ShortUUIDField(unique=True, length=5,
                         prefix="sku", alphabet="123456789")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50"/>')

    def __str__(self):
        return self.title

    def get_percentage(self):

        return int(((self.old_price - self.price) / self.old_price) * 100)


class ProductImages(models.Model):

    image = models.ImageField(upload_to="product-images")
    image_text = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=5)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating
