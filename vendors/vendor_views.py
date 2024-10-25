from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .processors.vendor_processor import (add_product, address, bankdetails,
                                          home, login, registration,
                                          show_products, delete_product, edit_product,
                                          vendor_orders, vendor_profile, product_images,
                                          update_extra_image, add_extra_images, delete_extra_images,
                                          earnings, monthly_earnings, weekly_earning, daily_earnings,
                                          payout_requests, vendor_product_reviews)
# Create your views here.

# for vendors


@login_required
def vendor_registration(request):

    return registration.processor(request)


@login_required
def vendor_bankdetails(request, vnd_id):

    return bankdetails.processor(request, vnd_id)


@login_required
def vendor_address(request, vnd_id):

    return address.processor(request, vnd_id)


@login_required
def vendor_home(request):

    return render(request, 'vendors/vendor_index.html', home.processor(request))


@login_required
def vendor_login(request):
    return login.processor(request)


@login_required
def add_vendor_product(request):

    return add_product.processor(request)


@login_required
def show_product(request):

    return show_products.processor(request)


@login_required
def delete_vendor_product(request):

    return delete_product.processor(request)


@login_required
def edit_vendor_product(request, prd_id):

    return edit_product.processor(request, prd_id)


@login_required
def show_vendor_orders(request):

    return vendor_orders.processor(request)


@login_required
def show_vendor_profile(request):

    return vendor_profile.processor(request)


@login_required
def show_product_images(request, prd_id):

    return product_images.processor(request, prd_id)


@login_required
def update_images(request, imageID):

    return update_extra_image.processor(request, imageID)


@login_required
def add_images(request, prd_id):

    return add_extra_images.processor(request, prd_id)


@login_required
def delete_images(request, prd_id):

    return delete_extra_images.processor(request, prd_id)


@login_required
def vendor_earnings(request):

    return earnings.processor(request)


@login_required
def vendor_weekly_earnings(request):

    return weekly_earning.processor(request)


@login_required
def vendor_monthly_earnings(request):

    return monthly_earnings.processor(request)


@login_required
def vendor_daily_earnings(request):

    return daily_earnings.processor(request)


@login_required
def payout(request):

    return payout_requests.processor(request)


@login_required
def show_product_reviews(request):

    return vendor_product_reviews.processor(request)
