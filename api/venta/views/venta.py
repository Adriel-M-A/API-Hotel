from rest_framework import viewsets
from apps.venta.models import Liquidacion, Factura, DetalleFactura, Alquiler, Pago
from api.venta.serializers.venta import (
    FacturaSerializer,
    LiquidacionSerializer,
    DetalleFacturaSerializer,
    PagoSerializer,
    AlquilerSerializer,
)


class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer


class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Liquidacion.objects.all()
    serializer_class = LiquidacionSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
