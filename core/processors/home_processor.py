from django.db.models import Avg
from core.models import Product, Category
from userauths.forms import loginForm, signupForm


def processor():
    toprated = Product.objects.annotate(average_rating=Avg(
        'productreview__rating')).filter(average_rating__gt=2)

    featured = Product.objects.filter(
        product_status='Published', featured=True)
    categories = Category.objects.all()
    latest = Product.objects.filter(
        product_status='Published').order_by('-date')

    def get_items(queryset, start, end):
        return {"items": queryset[start:end]}

    return {
        "featured": featured,
        "categories": categories,
        "latests": [get_items(latest, i, i+3) for i in range(0, 9, 3)],
        "topproducts": [get_items(toprated, i, i+3) for i in range(0, 9, 3)],
        "different": [get_items(latest, i, i+3) for i in range(9, 18, 3)],
        "loginform": loginForm(),
        "signupform": signupForm()
    }
