from django.shortcuts import redirect
from django.contrib import messages
from core.forms import ProductImagesForm


def processor(request, prd_id):
    if request.method == "POST":
        form = ProductImagesForm(
            request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.product_id = prd_id
            image.save()
            messages.success(request, 'New Image added successfully!!')
        else:
            messages.error(request, form.errors)

    return redirect(f"/vendor/product_images/{prd_id}")
