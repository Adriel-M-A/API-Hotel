from rest_framework import viewsets
from rest_framework.decorators import action
from apps.hotel.models import Hotel, Habitacion, Paquete, Temporada, Descuento
from api.hotel.serializers.hotel import (
    HotelSerializer,
    HabitacionSerializer,
    PaqueteSerializer,
    TemporadaSerializer,
    DescuentoSerializer,
    HotelMidSerializer,
    HotelFullSerializer,
)
from django_filters import rest_framework as filters
from api.hotel.filters.filters import HotelFilter


class HotelViewSet(viewsets.ModelViewSet):
    # Definimos el conjunto de datos y el serializador para el modelo Hotel
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelFilter

    # Visualizar todos los datos de todos los hoteles
    @action(detail=False, serializer_class=HotelFullSerializer)
    def full(self, request):
        return super().list(request)

    # Visualizar todos los datos de un único hotel
    @action(detail=True, url_path="full", serializer_class=HotelFullSerializer)
    def full_detail(self, request, pk=None):
        return super().retrieve(request, pk)

    # Visualizar datos intermedios de todos los hoteles
    @action(detail=False, serializer_class=HotelMidSerializer)
    def mid(self, request):
        return super().list(request)

    # Visualizar datos intermedios de un único hotel
    @action(detail=True, url_path="mid", serializer_class=HotelMidSerializer)
    def mid_detail(self, request, pk=None):
        return super().retrieve(request, pk)

    # Función para gestionar la disponibilidad de un hotel
    # @action(detail=True, methods=["post"], serializer_class=DisponibilidadSerializer)
    def disponibilidad(self, request, pk=None):
        # Validamos y guardamos los datos de disponibilidad
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        disp = serializer.save(hotel=self.get_object())
        # Devolvemos los datos de la oferta
        # serializer = OfertaSerializer(disp)
        # return Response(serializer.data)
        return 0


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
