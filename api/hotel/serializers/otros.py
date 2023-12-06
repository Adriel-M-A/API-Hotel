from rest_framework import serializers
from apps.hotel.models import Habitacion, Paquete, Temporada, Descuento

<<<<<<< HEAD
=======

>>>>>>> a14b2b48fbae9fc52eecf4bc3b245d82f3f3331a
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
