from rest_framework import serializers
from apps.hotel.models import Habitacion, Paquete, Temporada, Descuento, PrecioPorTipo

from core.serializers.otros import TipoHabitacionSerializer


class HabitacionSerializer(serializers.ModelSerializer):
    tipo = TipoHabitacionSerializer(read_only=True)

    class Meta:
        model = Habitacion
        fields = ["numero", "piso", "hotel", "tipo"]


class PaqueteSerializer(serializers.ModelSerializer):
    habitaciones = HabitacionSerializer(many=True, read_only=True)

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


class PrecioPorTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioPorTipo
        fields = ["tipo_habitacion", "precio"]
