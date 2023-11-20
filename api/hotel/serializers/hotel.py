from rest_framework import serializers
from apps.hotel.models import Hotel, Habitacion, Paquete, Temporada, Descuento
from api.core.serializers.ubicacion import UbicacionSerializer
from api.core.serializers.persona import VendedorSerializer, EncargadoSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class HotelFullSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer(source="*", read_only=True)
    encargado = EncargadoSerializer()
    vendedores = VendedorSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            "nombre",
            "encargado",
            "ubicacion",
            "descripcion",
            "tipos_habitacion",
            "habilitado",
            "vendedores",
        ]


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = "__all__"


class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = "__all__"


class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = "__all__"


class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = "__all__"
