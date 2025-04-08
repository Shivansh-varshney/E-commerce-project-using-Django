from django.urls import path
from . import views

urlpatterns = [
    #     general
    path("", views.home, name='home'),
    path("about/", views.about, name="about"),

    #     category
    path("category_products/<int:cat_id>",
         views.category_products_view, name="category_products"),
    path("category_products/", views.category_products_view,
         name="all_category_products"),

    #     orders
    path('orders/', views.orders_view, name='orders'),
    path('order_details/<oid>/', views.order_details_view, name='order_details'),

    #    products
    path("product/<int:prd_id>", views.product_view, name='product'),
    path("product_reviews/<int:prd_id>",
         views.product_reviews_view, name='product_reviews'),

    #     search
    path("search/", views.search_view, name="search"),
    path("tag/", views.show_tag_products, name="tag"),

    #     reviews
    path("ajax-add-review/<int:prd_id>",
         views.ajax_add_review, name='ajax-add-review'),
]
