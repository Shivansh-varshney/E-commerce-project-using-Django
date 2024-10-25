from django.http import JsonResponse
from django.template.loader import render_to_string


def processor(request):
    prd_id = request.GET['id']
    c_session = request.session
    cart_data = c_session['cart_data_obj']
    cart_total_amount = 0

    if "cart_data_obj" in c_session:
        if prd_id in cart_data:
            del cart_data[prd_id]
        c_session['cart_data_obj'] = cart_data

        for prd, item in c_session['cart_data_obj'].items():
            cart_total_amount += int(item['quantity']) * float(item['price'])

    context = render_to_string('cart/async/cart_list.html', {
                               'cart_data': request.session['cart_data_obj'],
                               'cart_total_amount': cart_total_amount,
                               'carttotalitems': len(request.session['cart_data_obj']),
                               'nav': 'hero-normal'
                               })
    return JsonResponse({
        "data": context
    })
