from . import vendor_views, customer_views
from django.urls import path

urlpatterns = [
    # for vendors

    # registration
    path('register/', vendor_views.vendor_registration, name='register'),
    path('bankdetails/<vnd_id>/',
         vendor_views.vendor_bankdetails, name='bankdetails'),
    path('address/<vnd_id>/', vendor_views.vendor_address, name='address'),

    # general
    path('login/', vendor_views.vendor_login, name='vendor_login'),
    path('home/', vendor_views.vendor_home, name='vendor_home'),
    path('profile/', vendor_views.show_vendor_profile, name='vendor_profile'),
    path('earnings/', vendor_views.vendor_earnings, name='vendor_earnings'),
    path('weekly/', vendor_views.vendor_weekly_earnings, name='weekly_earnings'),
    path('monthly/', vendor_views.vendor_monthly_earnings, name='monthly_earnings'),
    path('daily/', vendor_views.vendor_daily_earnings, name='daily_earnings'),
    path('payout/', vendor_views.payout, name='payout'),

    # product operations
    path('add/', vendor_views.add_vendor_product, name='add_product'),
    path('show_products/', vendor_views.show_product, name='show_products'),
    path('delete_product/', vendor_views.delete_vendor_product,
         name='delete_product/'),
    path('edit_product/<prd_id>/', vendor_views.edit_vendor_product,
         name='edit_product'),
    path('vendor_product_reviews/', vendor_views.show_product_reviews,
         name='vendor_product_reviews'),
    path('product_images/<prd_id>/', vendor_views.show_product_images,
         name='product_images'),
    path('add_images/<prd_id>/', vendor_views.add_images,
         name='add_images'),
    path('update_images/<imageID>/', vendor_views.update_images,
         name='update_images'),
    path('delete_images/<prd_id>', vendor_views.delete_images,
         name='delete_images'),

    # vendor orders
    path('orders/', vendor_views.show_vendor_orders, name='vendor_orders'),

    # for customers
    path("shops/", customer_views.all_shops_view, name='shops'),
    path("shop/<int:vnd_id>", customer_views.shop_view, name='shopproducts'),
    path('reviews/<vnd_id>', customer_views.vendor_reviews, name='vendor_review'),
    path('add_review/<vnd_id>', customer_views.add_review, name='add_review')
]
