from core.models import Product
from core.forms import UpdateProductForm
from django.shortcuts import redirect, render
from django.contrib import messages


def processor(request, prd_id):

    product = Product.objects.get(id=prd_id)

    if request.method == 'POST':
        form = UpdateProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            tags = form.cleaned_data.get('tags')
            if tags:
                product.tags.set(tags)

            messages.success(
                request, 'Product Updated Successfully')
        else:
            messages.error(request, form.errors)

        return redirect('/vendor/show_products/')

    else:

        form = UpdateProductForm(instance=product)
        context = {
            'form': form,
            'product': product
        }
        return render(request, 'vendors/edit_product.html', context)
