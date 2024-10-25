from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.urls')),
    path("cart/", include('cart.urls')),
    path("user/", include('userauths.urls')),
    path("payments/", include('payments.urls')),
    path("vendor/", include('vendors.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
