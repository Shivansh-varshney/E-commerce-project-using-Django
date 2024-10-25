from cart.models import CartOrder


def processor(request):
    orders = CartOrder.objects.filter(user_id=request.user).order_by('-date')

    return {
        'orders': orders
    }
