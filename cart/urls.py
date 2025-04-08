from django.urls import path
from . import views

urlpatterns = [
    # cart
    path("", views.cart_view, name="cart"),
    path("add_to_cart/", views.add_to_cart, name='add_to_cart'),
    path("delete_from_cart/", views.delete_from_cart, name='delete_from_cart'),
    path("delete_cart_data/<txnid>/",
         views.delete_cart_data, name='delete_cart_data'),
    path("delete_cart/",
         views.delete_cart, name='delete_cart'),
    path("update_cart/", views.update_cart, name='update_cart'),
]
