from django.shortcuts import render
from django.contrib import messages
from vendors.models import Vendor, vendorBankDetails, vendorAddress
from vendors.forms import vendorAddressForm, vendorbankdetailsForm


def processor(request, vnd_id):

    vendor_instance = vendorBankDetails.objects.get(vendor_id=vnd_id)

    if request.method == 'POST':
        form = vendorbankdetailsForm(request.POST, instance=vendor_instance)

        if form.is_valid():
            details = form.save(commit=False)
            details.vendor = Vendor.objects.get(pk=vnd_id)
            details.save()

            messages.success(request, 'Now add your business address!!')
            form = vendorAddressForm(
                instance=vendorAddress.objects.create(vendor=Vendor.objects.get(id=vnd_id)))
            context = {
                'form': form,
                'vnd_id': vnd_id,
                'step': 'address'
            }
            return render(request, 'vendors/registration.html', context)
        else:
            messages.error(request, form.errors)

    form = vendorbankdetailsForm(instance=vendor_instance)

    return render(request, 'vendors/registration.html', {
        'form': form,
        'vnd_id': vnd_id,
        'step': 'bankdetails'
    })
