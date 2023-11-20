from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/core/", include("api.core.routers.urls")),
    path("api/hotel/", include("api.hotel.routers.urls")),
    path("api/venta/", include("api.venta.routers.urls")),
]
