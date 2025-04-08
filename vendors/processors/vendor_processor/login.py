from vendors.models import Vendor
from django.http import Http404
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404


def processor(request):

    try:
        vendor = get_object_or_404(Vendor, user_id=request.user.id)

        return redirect(f'/vendor/home/')

    except Http404:
        return redirect('/vendor/register/')
