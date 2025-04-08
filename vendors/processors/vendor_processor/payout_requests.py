from django.shortcuts import redirect
from django.contrib import messages
from payments.models import payout_requests


def processor(request):

    if request.method == 'POST':

        amount = request.POST['amount']
        vendor = request.user.vendor

        payout = payout_requests.objects.create(
            vendor=vendor,
            amount=amount
        )

        payout.save()
        messages.success(
            request, 'Request sent successfully, You will recieve your payment within 24 hours.')

    return redirect('/vendor/earnings/')
