from django.shortcuts import redirect
from django.contrib import messages
from userauths.forms import loginForm
from django.contrib.auth import authenticate, login


def processor(request):
    if request.method == "POST":
        form = loginForm(request=request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")

        else:
            messages.error(
                request, 'Credentials not found. Try using different email or may be your password is wrong.')

    return redirect('/')
