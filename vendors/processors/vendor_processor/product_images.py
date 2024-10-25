from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Product, ProductImages
from core.forms import ProductThumbnailImageForm, ProductImagesForm


def processor(request, prd_id):

    product_instance = Product.objects.get(id=prd_id)

    if request.method == 'POST':
        thumbnailForm = ProductThumbnailImageForm(
            request.POST, request.FILES, instance=product_instance)

        if thumbnailForm.is_valid():
            thumbnailForm.save()
            messages.success(request, 'Thumbnail Updated Successfully')
            return redirect(f"/vendor/product_images/{prd_id}")

    thumbnailForm = ProductThumbnailImageForm()

    extraImagesForm = ProductImagesForm()

    extraImages = ProductImages.objects.filter(product_id=prd_id)

    context = {
        'mainImage': product_instance,
        'extraImages': extraImages,
        'thumbnailForm': thumbnailForm,
        'extraImagesForm': extraImagesForm
    }

    return render(request, 'vendors/product_images.html', context)
