from userauths.forms import signupForm
from django.contrib import messages
from django.shortcuts import redirect


def processor(request):
    if request.method == "POST":
        form = signupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!!')
            return redirect("/user/login/")

        else:
            messages.error(request, form.errors)

    return redirect('/')
