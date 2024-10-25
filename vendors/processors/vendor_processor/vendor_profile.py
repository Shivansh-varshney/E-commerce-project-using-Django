from django.shortcuts import render
from django.contrib import messages
from vendors.forms import changeRequestForm
from vendors.models import vendorAddress, vendorBankDetails, Vendor


def processor(request):

    if request.method == 'POST':
        form = changeRequestForm(request.POST)

        if form.is_valid():
            change_request = form.save(commit=False)
            change_request.vendor = request.user.vendor
            change_request.save()
            messages.success(request, 'Request raised successfully!!')
        else:
            messages.error(request, form.errors)

    vendor = request.user.vendor
    personal_details = Vendor.objects.get(pk=vendor.id)
    address = vendorAddress.objects.get(vendor_id=vendor.id)
    bankdetails = vendorBankDetails.objects.get(vendor_id=vendor.id)

    context = {
        'personal': personal_details,
        'address': address,
        'bankdetails': bankdetails,
        'form': changeRequestForm()
    }

    return render(request, 'vendors/vendor_profile.html', context)
