from django.urls import path
from . import views

urlpatterns = [

    # account actions
    path('profile/', views.profile_view, name='profile'),
    path('password/', views.change_password, name='password'),

    # address actions
    path('add_address/', views.add_address, name='add_address'),
    path('edit_address/<aid>', views.edit_address, name='edit_address'),
    path('delete_address/', views.delete_address, name='delete_address'),
    path('make_default/', views.make_default, name='make_default'),

    # basic actions
    path("signup/", views.signup_view, name='signup'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
]
