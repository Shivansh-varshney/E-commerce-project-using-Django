from django.http import JsonResponse
from userauths.models import CustomerAddress
from django.template.loader import render_to_string


def processor(request):
    aid = request.GET['aid']

    if 'contact' in request.session:
        request.session['contact']['address'] = aid
        request.session.save()

    context = render_to_string(
        'payments/async/shippingaddress.html', {
            'address': CustomerAddress.objects.get(id=aid)
        }
    )

    return JsonResponse({
        'data': context
    })
