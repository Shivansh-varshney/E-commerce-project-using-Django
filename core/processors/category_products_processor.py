from core.models import *


def processor(cat_id):

    products = Product.objects.filter(
        product_status='Published',
        category_id=cat_id
    ) if cat_id else Product.objects.filter(
        product_status='Published'
    )
    category = "All" if cat_id == 0 else Category.objects.get(
        pk=cat_id).title
    categories = Category.objects.all()

    return {
        "products": products,
        "categories": categories,
        "categoryname": category,
    }
