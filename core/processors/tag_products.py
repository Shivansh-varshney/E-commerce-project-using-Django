from core.models import Product
from django.shortcuts import render
# from taggit.models import TaggedItem


def processor(request):

    tag = request.GET['tag']

    tagged_products = Product.objects.filter(tags__name__in=[tag])

    return render(request, 'core/search.html', {'products': tagged_products, 'query': tag})
