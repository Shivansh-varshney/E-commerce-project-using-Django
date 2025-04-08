from django.utils import timezone
from django.db.models.functions import Cast
from django.db.models import F, Sum, IntegerField

from cart.models import CartOrderItems

from core.models import Product
from core.forms import ProductForm

from vendors.models import Vendor
from vendors.models import vendor_review

start_of_today = timezone.now().replace(
    hour=0, minute=0, second=0, microsecond=0)
end_of_today = timezone.now().replace(
    hour=23, minute=59, second=59, microsecond=999999)


def processor(request):

    vendor = request.user.vendor

    reviews = vendor_review.objects.filter(
        vendor_id=vendor.id).order_by('-date')

    recent_products = Product.objects.filter(
        cartorderitems__order__date__range=(
            start_of_today, end_of_today),  # Filter by today's date
        vendor=vendor  # Filter by specified vendor
    ).annotate(quantity=F('cartorderitems__qty'),
               orderid=F('cartorderitems__order__id'),
               total=F('cartorderitems__total'))

    total_orders = CartOrderItems.objects.filter(
        product__vendor=vendor, order__order_status="Delivered"
    ).aggregate(total_sold=Sum(Cast('qty', output_field=IntegerField())))['total_sold']

    total_products = Product.objects.filter(
        vendor=vendor, product_status='Published'
    ).count()

    revenue = CartOrderItems.objects.filter(
        product__vendor=vendor
    ).aggregate(total_income=Sum('total'))['total_income']

    if revenue is not None:
        int(revenue)
    else:
        revenue = 0

    return {
        'vendor': Vendor.objects.get(user_id=request.user.id),
        'recents': recent_products,
        'form': ProductForm(),
        'total_orders': total_orders,
        'total_products': total_products,
        'reviews': reviews[:5],
        'revenue': revenue
    }
