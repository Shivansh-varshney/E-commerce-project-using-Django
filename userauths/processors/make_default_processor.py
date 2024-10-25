from userauths.forms import customerAddress
from userauths.models import CustomerAddress
from django.template.loader import render_to_string

def processor(request):
    aid = request.GET['aid']

    try:
        current_default = CustomerAddress.objects.get(
            user_id=request.user.id, status=True)
        current_default.status = False
        current_default.save()
    except Exception:
        current_default = None

    make_default = CustomerAddress.objects.get(id=aid, user_id=request.user.id)
    make_default.status = True
    make_default.save()

    return render_to_string(
        'userauths/async/addresslist.html', {
            'addresses': CustomerAddress.objects.filter(user_id=request.user.id),
            'addressform': customerAddress()
        }
    )