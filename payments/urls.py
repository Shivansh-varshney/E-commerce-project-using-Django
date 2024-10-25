from . import views
from django.urls import path

# payment urls

urlpatterns = [
    path("payment_request/", views.payment_request, name='payment_request'),
    path("successfull/", views.successful_payment, name='successful'),
    path("failure/", views.failed_payment, name='failure'),
    path("successfull/<attempt>", views.successful_payment, name='successful'),
    path("failure/<attempt>", views.failed_payment, name='failure'),
    path('shipping_address/', views.shipping_address, name='shipping_address'),

    # check out
    path("checkout/", views.checkout_view, name='checkout'),
]
