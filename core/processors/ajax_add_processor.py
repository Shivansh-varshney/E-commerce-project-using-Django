from datetime import datetime
from django.http import JsonResponse
from core.models import Product, ProductReview

now = datetime.now()


def processor(request, prd_id):
    product = Product.objects.get(pk=prd_id)
    user = request.user
    review = request.POST['review']
    rating = request.POST['rating']

    ProductReview.objects.create(
        user=user, product=product, review=review, rating=rating)

    return JsonResponse({
        'context': {
            "user": user.first_name,
            "review": review,
            "rating": rating,
            "date": now.strftime("%Y-%m-%d %H:%M:%S")
        },
        'bool': True})
