from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.hotel.views.hotel import (
    HotelViewSet,
    HabitacionViewSet,
    PaqueteViewSet,
    DescuentoViewSet,
    TemporadaViewSet,
)

router = DefaultRouter()
router.register(r"hoteles", HotelViewSet)
router.register(r"habitaciones", HabitacionViewSet)
router.register(r"paquetes", PaqueteViewSet)
router.register(r"descuentos", DescuentoViewSet)
router.register(r"temporadas", TemporadaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
