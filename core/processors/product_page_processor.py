from django.db.models import Avg
from core.forms import ProductReviewForm
from core.models import Product, ProductReview, ProductImages


def processor(user, prd_id):
    product = Product.objects.get(pk=prd_id)

    product_review = ProductReview.objects.filter(
        product=prd_id).order_by('-date')

    product_images = ProductImages.objects.filter(product_id=prd_id)

    related_products = Product.objects.filter(
        category=product.category, product_status='Published').exclude(pk=prd_id).order_by('-date')

    vendor_products = Product.objects.filter(
        vendor_id=product.vendor.id, product_status='Published').exclude(pk=prd_id).order_by('-date')

    fields = ["manufacturer", "manufactured",
              "expiring", "warranty_period", "return_options", "size"]

    valid_field = {field.capitalize(): getattr(product, field) for field in fields if getattr(
        product, field)}

    stars = {
        1: "⭐✯✯✯✯",
        2: "⭐⭐✯✯✯",
        3: "⭐⭐⭐✯✯",
        4: "⭐⭐⭐⭐✯",
        5: "⭐⭐⭐⭐⭐"
    }

    try:
        average = ProductReview.objects.filter(
            product_id=prd_id).aggregate(rating=Avg('rating'))
        rating = stars[int(average['rating'])]
    except Exception:
        rating = 'No reviews'

    form = False if user.is_anonymous or ProductReview.objects.filter(
        user=user, product=prd_id).count() else ProductReviewForm()

    return {
        "product": product,
        "reviews_count": product_review,
        "reviews": product_review[:5],
        "related": related_products,
        'from_vendor': vendor_products,
        "images": product_images,
        "fields": valid_field,
        "stars": rating,
        "form": form
    }
