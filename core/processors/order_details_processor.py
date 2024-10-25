from cart.models import CartOrder, CartOrderItems


def processor(request, oid):
    order = CartOrder.objects.get(id=oid)
    order_items = CartOrderItems.objects.filter(order_id=oid)

    return {
        'order': order,
        'items': order_items,
    }
