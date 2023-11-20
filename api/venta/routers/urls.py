from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.venta.views.venta import (
    AlquilerViewSet,
    FacturaViewSet,
    DetalleFacturaViewSet,
    LiquidacionViewSet,
    PagoViewSet,
)


router = DefaultRouter()
router.register(r"alquileres", AlquilerViewSet)
router.register(r"facturas", FacturaViewSet)
router.register(r"destalles", DetalleFacturaViewSet)
router.register(r"liquidaciones", LiquidacionViewSet)
router.register(r"pagos", PagoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
