from core.models import Product
from django.shortcuts import redirect
from payments.models import transactions
from userauths.models import CustomerAddress
from cart.models import CartOrder, CartOrderItems


def processor(request, txnid):
    c_session = request.session
    cart_total_amount = 0

    if "cart_data_obj" in c_session:
        cart_data = c_session['cart_data_obj']
        for prd_id, item in cart_data.items():
            cart_total_amount += int(item['quantity']) * \
                float(item['price'])

        order = CartOrder.objects.create(
            user=request.user,
            txnid=txnid,
            name=c_session['contact']['name'],
            phone=c_session['contact']['phone'],
            email=c_session['contact']['email'],
            address=CustomerAddress.objects.get(
                id=request.session['contact']['address']),
            price=cart_total_amount,
            paid_status=True,
        )

        transaction = transactions.objects.get(txnid=txnid)
        transaction.order = order
        transaction.save()

        for prd_id, item in cart_data.items():
            order_item = CartOrderItems.objects.create(
                order=order,
                product=Product.objects.get(id=prd_id),
                qty=item['quantity'],
                price=item['price'],
                total=int(item['quantity']) *
                float(item['price'])
            )

            product = Product.objects.get(id=prd_id)
            product.stock_quantity -= int(item['quantity'])
            product.save()

        c_session['cart_data_obj'] = {}
        c_session['contact'] = {
            'name': '',
            'phone': '',
            'email': '',
            'address': ''
        }

    return redirect(f'/order_details/{order.id}/')
