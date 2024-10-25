from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .processors import (change_password_processor, signup_processor, login_processor, add_address_processor,
                         delete_address_processor, edit_address_processor, make_default_processor, profile_processor)
# Create your views here.


def signup_view(request):
    return signup_processor.processor(request)


def login_view(request):
    return login_processor.processor(request)


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def profile_view(request):

    return render(request, 'userauths/profile.html', profile_processor.processor(request))


@login_required
def add_address(request):

    return add_address_processor.processor(request)


@login_required
def edit_address(request, aid):

    return edit_address_processor.processor(request, aid)


@login_required
def delete_address(request):

    return JsonResponse({
        'data': delete_address_processor.processor(request)
    })


@login_required
def make_default(request):

    return JsonResponse({
        'data': make_default_processor.processor(request)
    })


@login_required
def change_password(request):
    return change_password_processor.processor(request)
