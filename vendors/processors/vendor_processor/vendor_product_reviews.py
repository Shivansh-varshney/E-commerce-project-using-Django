from core.models import ProductReview
from django.http import JsonResponse
from django.template.loader import render_to_string


def processor(request):

    prd_id = request.GET['prd_id']

    reviews = ProductReview.objects.filter(product_id=prd_id)

    context = render_to_string('vendors/async/product_reviews.html', {
        'reviews': reviews
    })

    return JsonResponse(
        {
            'data': context
        }
    )
