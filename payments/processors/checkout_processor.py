from userauths.models import CustomerAddress


def processor(request):
    cart_total_amount = 0
    cart_name = ''
    
    for prd_id, item in request.session['cart_data_obj'].items():
        cart_total_amount += int(item['quantity']) * float(item['price'])
        cart_name += str(item['title']) + ',\n'

    try:
        address = CustomerAddress.objects.get(
            user_id=request.user.id, status=True)

    except Exception:
        address = False

    addresses = CustomerAddress.objects.filter(
        user_id=request.user.id) if address else None

    return {
        'cart_data': request.session['cart_data_obj'],
        'cart_total_amount': cart_total_amount,
        'cart_name': cart_name,
        'addresses': addresses,
        'address': address,
    }
