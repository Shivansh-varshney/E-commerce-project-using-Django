from core.models import Product
from django.db.models import Q


def processor(query):
    query.capitalize()
    products = Product.objects.filter(
        Q(title__icontains=query) |
        Q(vendor__title__icontains=query) |
        Q(category__title__iexact=query)
    ).order_by("-date").distinct()

    return {
        "products": products,
        "query": query,
    }
