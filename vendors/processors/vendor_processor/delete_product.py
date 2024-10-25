from django.http import JsonResponse
from core.models import Product
from django.template.loader import render_to_string


def processor(request):

    prd_id = request.GET['pid']
    product = Product.objects.get(id=prd_id)
    product.delete()

    vendor_id = request.user.vendor.id
    products = Product.objects.filter(vendor_id=vendor_id).order_by('-id')

    context = render_to_string(
        'vendors/async/products.html', {
            'products': products
        }

    )

    return JsonResponse({
        'data': context
    })
