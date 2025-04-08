from cart.models import *
from django.shortcuts import render
from userauths.forms import loginForm, signupForm
from django.contrib.auth.decorators import login_required

from .processors import (ajax_add_processor, category_products_processor, home_processor,
                         order_details_processor, orders_processor, search_processor,
                         product_page_processor, product_reviews_processor, tag_products)

# Create your views here.


def about(request):
    context = {
        "loginform": loginForm(),
        "signupform": signupForm()
    }
    return render(request, 'core/about.html', context)


@login_required
def ajax_add_review(request, prd_id):

    return ajax_add_processor.processor(request, prd_id)


def category_products_view(request, cat_id=0):

    return render(request, "core/category_products.html", category_products_processor.processor(cat_id))


def home(request):

    return render(request, 'core/index.html', home_processor.processor())


@login_required
def order_details_view(request, oid):

    return render(request, 'core/order_details.html', order_details_processor.processor(request, oid))


@login_required
def orders_view(request):

    return render(request, 'core/orders.html', orders_processor.processor(request))


def product_view(request, prd_id):

    return render(request, 'core/product.html', product_page_processor.processor(request.user, prd_id))


def product_reviews_view(request, prd_id):

    return render(request, 'core/reviews.html', product_reviews_processor.processor(request, prd_id))


def search_view(request):

    return render(request, "core/search.html", search_processor.processor(request.GET['query']))


def show_tag_products(request):

    return tag_products.processor(request)
