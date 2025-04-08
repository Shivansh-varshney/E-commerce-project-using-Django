from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .processors import (cart_view_processor,
                         add_to_cart_processor, delete_from_cart_processor,
                         delete_cart_data_processor, update_cart_processor
                         )
# Create your views here.


def add_to_cart(request):

    return add_to_cart_processor.processor(request)


@login_required
def cart_view(request):

    return render(request, "cart/cart.html", cart_view_processor.processor(request))


@login_required
def delete_from_cart(request):

    return delete_from_cart_processor.processor(request)


def delete_cart_data(request, txnid):

    return delete_cart_data_processor.processor(request, txnid)


@login_required
def update_cart(request):

    return update_cart_processor.processor(request)


@login_required
def delete_cart(request):

    c_session = request.session
    cart_total_amount = 0

    if "cart_data_obj" in c_session:
        cart_data = c_session['cart_data_obj']

        c_session['cart_data_obj'] = {}
        c_session['contact'] = {}

    return redirect('/')
