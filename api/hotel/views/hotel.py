from rest_framework import viewsets
from apps.hotel.models import Hotel, Habitacion, Paquete, Temporada, Descuento
from api.hotel.serializers.hotel import (
    HotelSerializer,
    HabitacionSerializer,
    PaqueteSerializer,
    TemporadaSerializer,
    DescuentoSerializer,
)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


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
