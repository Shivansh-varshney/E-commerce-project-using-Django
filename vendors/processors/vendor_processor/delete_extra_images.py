from django.contrib import messages
from django.shortcuts import redirect
from core.models import ProductImages


def processor(request, prd_id):

    image_id = request.GET['prd_id']

    ProductImages.objects.get(id=image_id).delete()

    messages.success(request, 'Image deleted!!')
    return redirect(f"/vendor/product_images/{prd_id}")
