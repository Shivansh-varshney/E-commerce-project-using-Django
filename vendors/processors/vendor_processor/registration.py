from django.shortcuts import render
from django.contrib import messages
from vendors.models import vendorBankDetails
from vendors.forms import VendorForm, vendorbankdetailsForm


def processor(request):

    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)

        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()

            messages.success(request, 'Now add you bank details!!')
            form = vendorbankdetailsForm(
                instance=vendorBankDetails.objects.create(vendor=vendor))

            context = {
                'form': form,
                'vnd_id': vendor.id,
                'step': 'bankdetails'
            }

            return render(request, 'vendors/registration.html', context)
        else:

            messages.error(request, form.errors)

    form = VendorForm()

    return render(request, 'vendors/registration.html',  {
        'form': form,
        'step': 'register'
    })
