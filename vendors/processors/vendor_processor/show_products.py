from django.shortcuts import render
from core.forms import ProductForm
from core.models import Product, ProductReview


def processor(request):

    vnd_id = request.user.vendor.id

    products = Product.objects.filter(vendor_id=vnd_id).order_by('-id')
    productreviews = ProductReview.objects.filter(
        product__vendor_id=vnd_id
    ).order_by('-id')

    context = {
        'products': products,
        'reviews': productreviews,
        'form': ProductForm
    }

    return render(request, 'vendors/show_products.html', context)
