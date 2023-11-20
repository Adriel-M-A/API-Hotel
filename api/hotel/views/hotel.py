from rest_framework import viewsets
from rest_framework.decorators import action
from apps.hotel.models import Hotel, Habitacion, Paquete, Temporada, Descuento
from api.hotel.serializers.hotel import (
    HotelSerializer,
    HabitacionSerializer,
    PaqueteSerializer,
    TemporadaSerializer,
    DescuentoSerializer,
    HotelFullSerializer,
)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=True, url_path="full", serializer_class=HotelFullSerializer)
    def full_detail(self, request, pk=None):
        return super().retrieve(request, pk)


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


class PaqueteViewSet(viewsets.ModelViewSet):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer


class TemporadaViewSet(viewsets.ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer


class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
