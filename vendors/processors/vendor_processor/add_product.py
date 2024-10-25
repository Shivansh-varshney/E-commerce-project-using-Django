from django.shortcuts import redirect
from django.contrib import messages
from core.forms import ProductForm


def processor(request):

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.product_status = 'In review'
            product.save()

            form.save_m2m()
            tags = form.cleaned_data.get('tags')
            if tags:
                product.tags.set(tags)

            messages.success(
                request, 'Product has been submitted for review, We will Publish your product within 24 hours!!')
        else:

            messages.error(request, form.errors)

    return redirect('/vendor/show_products/')
