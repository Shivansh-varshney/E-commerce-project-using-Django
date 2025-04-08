from django.shortcuts import render
from vendors.models import vendor_review
from django.core.paginator import Paginator


def processor(request, vnd_id):

    reviews = vendor_review.objects.filter(vendor_id=vnd_id).order_by('-date')
    paginator = Paginator(reviews, 15)  # Show 10 reviews per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'vendors/reviews.html', {
        'page_obj': page_obj,
        'vendor': vnd_id
    })
