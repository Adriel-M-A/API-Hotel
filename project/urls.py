from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("api.core.routers.urls")),
    path("hotel/", include("api.hotel.routers.urls")),
    path("venta/", include("api.venta.routers.urls")),
]
