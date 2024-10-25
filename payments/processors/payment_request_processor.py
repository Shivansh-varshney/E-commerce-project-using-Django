import random
from django.shortcuts import render
from payments.models import transactions


def generate_txnid():

    alphanums = 'abcdefghjklmnpqrstuvwxyz23456789'
    txnid = ''

    for i in range(8):
        txnid += alphanums[random.randint(0, len(alphanums)-1)]

    return txnid


def processor(request, payu, surl, furl):
    if request.method == 'POST':
        # Making Checkout form into dictionary
        data = {k: v[0] for k, v in dict(request.POST).items()}

        request.session['contact']['name'] = request.POST['firstname'] + ' ' +\
            request.POST['lastname']
        request.session['contact']['phone'] = request.POST['phone']
        request.session['contact']['email'] = request.POST['email']
        request.session.save()
        
        data['surl'] = surl
        data['furl'] = furl

        txnid = generate_txnid()

        data.update({"txnid": txnid})

        transaction = transactions.objects.create(
            user=request.user,
            txnid=txnid
        )

        transaction.save()

        payu_data = payu.transaction(**data)
        
        return render(request, 'payments/payu.html', {"posted": payu_data})
