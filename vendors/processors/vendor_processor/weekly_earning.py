from cart.models import CartOrderItems
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models.functions import TruncWeek
from django.template.loader import render_to_string


def processor(request):

    vendor = request.user.vendor

    earnings = CartOrderItems.objects.filter(
        product__vendor=vendor
    ).annotate(
        week=TruncWeek('date')
    ).values('week').annotate(
        total_earnings=Sum('price')
    ).order_by('-week')

    context = render_to_string(
        'vendors/async/weekly.html', {
            'earnings': earnings,
        })

    return JsonResponse(
        {
            'data': context
        }
    )
