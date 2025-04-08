from django.shortcuts import redirect
from django.contrib import messages
from core.models import ProductImages
from core.forms import ProductImagesForm


def processor(request, imageID):

    image_instance = ProductImages.objects.get(id=imageID)
    prd_id = image_instance.product_id

    if request.method == "POST":
        form = ProductImagesForm(
            request.POST, request.FILES, instance=image_instance)

        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated successfully!!')
        else:
            messages.error(request, form.errors)

    return redirect(f"/vendor/product_images/{prd_id}")
