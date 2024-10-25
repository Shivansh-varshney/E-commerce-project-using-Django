from django.shortcuts import redirect
from django.contrib import messages
from userauths.forms import customerAddress


def processor(request):
    if request.method == "POST":
        form = customerAddress(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()

            messages.success(request, 'Address Added successfully!!')
        else:
            messages.error(request, form.errors)

    return redirect('/user/profile/')
