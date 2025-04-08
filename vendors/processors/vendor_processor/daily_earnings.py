from cart.models import CartOrderItems
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models.functions import TruncDay
from django.template.loader import render_to_string


def processor(request):

    vendor = request.user.vendor

    earnings = CartOrderItems.objects.filter(
        product__vendor=vendor
    ).annotate(
        day=TruncDay('date')
    ).values('day').annotate(
        total_earnings=Sum('price')
    ).order_by('-day')

    context = render_to_string(
        'vendors/async/daily.html', {
            'earnings': earnings,
        })

    return JsonResponse(
        {
            'data': context
        }
    )
