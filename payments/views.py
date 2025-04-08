from payments.paywix.payu import Payu
from ecommerce import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .processors import (checkout_processor, payment_request_processor,
                         shipping_processor, failed_payment_processor,
                         successful_payment_processor)

# Create your views here.
# payu payment gateway integration

merchant_key = settings.MERCHANT_KEY
merchant_salt = settings.MERCHANT_SALT
mode = settings.MERCHANT_MODE
surl = settings.RESPONSE_URL_SUCCESS
furl = settings.RESPONSE_URL_FAILURE
payu = Payu(merchant_key, merchant_salt, mode)


@login_required
def checkout_view(request):

    return render(request, 'payments/checkout.html', checkout_processor.processor(request))


@login_required
def shipping_address(request):

    return shipping_processor.processor(request)


@csrf_exempt
def payment_request(request):

    return payment_request_processor.processor(request, payu, surl, furl)


@csrf_exempt
def successful_payment(request, attempt=0):
    return successful_payment_processor.processor(request, attempt)


@csrf_exempt
def failed_payment(request, attempt=0):
    return failed_payment_processor.processor(request, attempt)
