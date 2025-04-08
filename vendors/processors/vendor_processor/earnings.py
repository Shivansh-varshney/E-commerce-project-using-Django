from django.db.models import Sum
from django.shortcuts import render
from .monthly_earnings import month_earnings
from cart.models import CartOrderItems
from django.db.models.functions import TruncMonth


def processor(request):

    vendor = request.user.vendor

    earnings = month_earnings(request, vendor)

    total_months = 0
    for month in earnings:
        total_months += 1

    revenue = CartOrderItems.objects.filter(
        product__vendor=vendor
    ).aggregate(total_income=Sum('total'))['total_income']

    # average revenue per month
    if revenue:
        average = revenue/total_months
    else:
        average = 0
        revenue = 0

    context = {
        'earnings': earnings,
        'revenue': revenue,
        'average': average,
        'monthly': 'active',
        'vendor': vendor
    }

    return render(request, 'vendors/earnings.html', context)
