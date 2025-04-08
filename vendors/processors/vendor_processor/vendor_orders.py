from django.db.models import F, ExpressionWrapper, DateField, Func
from django.shortcuts import render
from datetime import timedelta
from cart.models import CartOrderItems


def processor(request):

    vendor = request.user.vendor

    all_orders = CartOrderItems.objects.filter(
        product__vendor=vendor  # Filter by specified vendor
    ).annotate(orderid=F('order__id'),
               productid=F('product__pid'),
               status=F('order__order_status'),
               txnid=F('order__txnid'),
               pickdate=ExpressionWrapper(
                   Func(
                       F('date') + timedelta(days=2),
                       function='DATE'
                   ),
                   output_field=DateField())).order_by('-orderid')

    context = {
        'orders': all_orders
    }

    return render(request, 'vendors/vendor_orders.html', context)
