from django.shortcuts import redirect
from django.contrib import messages
from vendors.models import Vendor, vendor_review
from vendors.forms import vendorreviewForm


def processor(request, vnd_id):

    if request.method == 'POST':
        reviewform = vendorreviewForm(request.POST)

        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.user = request.user
            review.vendor = Vendor.objects.get(id=vnd_id)

            review.save()
            messages.success(request, 'Review added!!')

        else:
            messages.error(request, reviewform.errors)

    return redirect(f'/vendor/shop/{vnd_id}')
