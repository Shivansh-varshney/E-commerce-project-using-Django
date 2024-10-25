from django.core.paginator import Paginator
from core.models import Product, ProductReview


def processor(request, prd_id):

    product = Product.objects.get(pk=prd_id)
    product_review = ProductReview.objects.filter(
        product=prd_id).order_by('-date')

    paginator = Paginator(product_review, 15)  # Show 10 reviews per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return {
        "product": product,
        'page_obj': page_obj
    }
