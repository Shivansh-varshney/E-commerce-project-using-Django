from django.shortcuts import redirect
from django.contrib import messages
from userauths.forms import updatePasswordForm


def processor(request):
    if request.method == "POST":
        form = updatePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed!!')

        else:
            messages.error(
                request, f"{form.errors}")

    return redirect('/user/profile/')
