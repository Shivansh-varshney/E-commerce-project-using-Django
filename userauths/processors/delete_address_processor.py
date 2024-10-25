from userauths.models import CustomerAddress
from userauths.forms import customerAddress
from django.template.loader import render_to_string


def processor(request):
    aid = request.GET['aid']

    address_instance = CustomerAddress.objects.get(id=aid)

    address_instance.delete()

    return render_to_string(
        'userauths/async/addresslist.html', {
            'addresses': CustomerAddress.objects.filter(user_id=request.user.id),
            'addressform': customerAddress()
        }
    )
