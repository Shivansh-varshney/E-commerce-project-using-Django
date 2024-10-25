from django.shortcuts import redirect, render
from django.contrib import messages
from vendors.forms import vendorAddressForm
from vendors.models import Vendor, vendorAddress


def processor(request, vnd_id):
    vendor_instance = vendorAddress.objects.get(vendor_id=vnd_id)

    if request.method == 'POST':
        form = vendorAddressForm(request.POST, instance=vendor_instance)

        if form.is_valid():
            details = form.save(commit=False)
            details.vendor = Vendor.objects.get(pk=vnd_id)
            details.save()

            messages.success(request, 'Vendor account created successfull!!')

            return redirect('/vendor/home/')
        else:
            messages.error(request, form.errors)

    form = vendorAddressForm(instance=vendor_instance)

    return render(request, 'vendors/registration.html',  {
        'form': form,
        'vnd_id': vnd_id,
        'step': 'address'
    })
