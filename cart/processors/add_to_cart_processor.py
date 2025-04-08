from userauths.models import CustomerAddress
from django.http import JsonResponse


def processor(request):

    prd_id = str(request.GET["id"])

    cart_product = {
        prd_id: {
            'title': request.GET['title'],
            'quantity': request.GET['quantity'],
            'price': request.GET['price']
        },
    }

    contact = {
        'name': '',
        'phone': '',
        'email': '',
        'address': ''
    }

    if request.user.is_authenticated:

        if 'cart_data_obj' in request.session:
            cart_data = request.session['cart_data_obj']

            if prd_id in cart_data:
                cart_data[prd_id]['quantity'] = int(cart_data[prd_id]['quantity']) + int(
                    cart_product[prd_id]['quantity'])

            else:
                cart_data.update(cart_product)

            request.session['cart_data_obj'] = cart_data

        else:
            request.session['cart_data_obj'] = cart_product

        address = CustomerAddress.objects.filter(
            user_id=request.user.id, status=True).first()

        if 'contact' in request.session:
            
            if 'address' in request.session['contact']:
                request.session['contact']['address'] = address.id if address else None
        else:
            request.session['contact'] = contact
            request.session['contact']['address'] = address.id if address else None

        return JsonResponse({
            "data": request.session['cart_data_obj'],
            "bool": True
        })

    return JsonResponse({
        "data": "Login first.",
        "bool": False
    })
