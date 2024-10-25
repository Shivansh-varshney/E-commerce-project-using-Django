from django.contrib import admin
from .models import Category, Product, ProductImages, ProductReview

# Register your models here.


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['vendor', 'title',
                    'product_image', 'stock_quantity', 'featured',  "category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cid', 'title', 'category_image']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating', 'date']
