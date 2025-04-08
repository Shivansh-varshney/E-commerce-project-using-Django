from django.contrib import messages
from userauths.forms import customerAddress
from userauths.models import CustomerAddress
from django.shortcuts import redirect, render


def processor(request, aid):
    address_instance = CustomerAddress.objects.get(id=aid)

    if request.method == "POST":
        addressform = customerAddress(request.POST, instance=address_instance)
        if addressform.is_valid():
            addressform.save()
            messages.success(request, 'Address changed successfully!!')
        else:
            messages.error(request, addressform.errors)

        return redirect('/user/profile/')

    return render(request, 'userauths/address.html', {
        'form': customerAddress(instance=address_instance),
        'address': address_instance,
    })
