from core.models import Product
from django.db.models import Avg
from vendors.forms import vendorreviewForm
from vendors.models import Vendor, vendor_review
from userauths.forms import loginForm, signupForm


def processor(request, vnd_id):
    user = request.user

    stars = {
        1: "⭐✯✯✯✯",
        2: "⭐⭐✯✯✯",
        3: "⭐⭐⭐✯✯",
        4: "⭐⭐⭐⭐✯",
        5: "⭐⭐⭐⭐⭐"
    }

    try:
        average = vendor_review.objects.filter(
            vendor_id=vnd_id).aggregate(rating=Avg('rating'))
        reviews = vendor_review.objects.filter(
            vendor_id=vnd_id).order_by('-date')[:5]
        stars = stars[int(average['rating'])]
    except Exception:
        stars = 'No reviews'

    return {
        "products": Product.objects.filter(vendor=vnd_id),
        "vendor": Vendor.objects.get(pk=vnd_id),
        'average': stars,
        'reviews': reviews,
        'reviewform': False if user.is_anonymous or vendor_review.objects.filter(
            user=user, vendor=vnd_id).count() else vendorreviewForm(),
        'loginform': loginForm(),
        'signupform': signupForm()
    }
