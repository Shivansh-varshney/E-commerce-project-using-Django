from .models import Vendor
from django.shortcuts import render
from userauths.forms import loginForm, signupForm
from django.contrib.auth.decorators import login_required

from .processors.customer_processors import (
    shop_processor, add_review_processor,
    vendor_reviews_processor)


def shop_view(request, vnd_id):

    return render(request, "vendors/shop_products.html", shop_processor.processor(request, vnd_id))


def all_shops_view(request):

    context = {
        'loginform': loginForm(),
        'signupform': signupForm(),
        "shops": Vendor.objects.all().reverse()
    }
    return render(request, 'vendors/shop.html', context)


@ login_required
def add_review(request, vnd_id):

    return add_review_processor.processor(request, vnd_id)


@ login_required
def vendor_reviews(request, vnd_id):
    return vendor_reviews_processor.processor(request, vnd_id)
