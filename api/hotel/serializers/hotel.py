from rest_framework import serializers
from apps.hotel.models import Hotel, Habitacion, Paquete, Temporada, Descuento


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


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
