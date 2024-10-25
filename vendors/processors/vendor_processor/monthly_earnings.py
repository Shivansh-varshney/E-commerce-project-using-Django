from django.db.models import Sum
from django.http import JsonResponse
from cart.models import CartOrderItems
from django.db.models.functions import TruncMonth
from django.template.loader import render_to_string


def month_earnings(request, vendor):

    earnings = CartOrderItems.objects.filter(
        product__vendor=vendor
    ).annotate(
        month=TruncMonth('date')  # Extract the month from the order date
    ).values('month').annotate(
        total_earnings=Sum('price')
    ).order_by('-month')

    return earnings


def processor(request):
    vendor = request.user.vendor

    earnings = month_earnings(request, vendor)

    context = render_to_string(
        'vendors/async/monthly.html', {
            'earnings': earnings,
        })

    return JsonResponse(
        {
            'data': context
        }
    )
