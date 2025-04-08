from payments.paywix.payu import Payu
from ecommerce import settings
from payments.models import transactions
from django.shortcuts import render, redirect

merchant_key = settings.MERCHANT_KEY
merchant_salt = settings.MERCHANT_SALT
mode = settings.MERCHANT_MODE
surl = settings.RESPONSE_URL_SUCCESS
furl = settings.RESPONSE_URL_FAILURE
payu = Payu(merchant_key, merchant_salt, mode)


def processor(request, attempt):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_payment(**data)

    transaction_details = response.get('transaction_details', {})

    try:
        transaction_id = list(transaction_details.keys())[0]
        status = transaction_details[transaction_id].get('status', 'failed')

        if status == 'failed':
            transaction = transactions.objects.get(txnid=transaction_id)
            context = {
                'message1': 'Payment Failed.',
                'message2': 'We couldn\'t verify your payment on our Side. Kindly contact our customer support team.',
                'txnid': transaction.txnid
            }

            return render(request, 'payments/payment-failure.html')

    except IndexError:

        if attempt < 5:
            return redirect(f'/payments/successfull/{attempt+1}')

        else:
            transaction = transactions.objects.get(txnid=transaction_id)
            context = {
                'message1': 'Payment not verified.',
                'message2': 'We couldn\'t verify your payment on our Side. Kindly contact our customer support team.',
                'txnid': transaction.txnid
            }
            return render(request, 'payments/payment-failure.html', context)
