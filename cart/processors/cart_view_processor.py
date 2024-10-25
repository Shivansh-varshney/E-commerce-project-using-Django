def processor(request):
    cart_total_amount = 0
    context = {}

    if "cart_data_obj" in request.session:
        
        for prd_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['quantity']) * float(item['price'])

        context['cart_data'] = request.session['cart_data_obj']
        context['cart_total_amount'] = cart_total_amount
        context['carttotalitems'] = len(request.session['cart_data_obj'])

    return context
