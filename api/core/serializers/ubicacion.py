from rest_framework import serializers
from apps.core.models import (
    Pais,
    Provincia,
    Ciudad,
    Direccion,
)


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = "__all__"


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = "__all__"


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"


class UbicacionSerializer(serializers.Serializer):
    pais = serializers.CharField(source="direccion.ciudad.provincia.pais.nombre")
    provincia = serializers.CharField(source="direccion.ciudad.provincia.nombre")
    ciudad = serializers.CharField(source="direccion.ciudad.nombre")
    calle = serializers.CharField(source="direccion.calle")
    numero = serializers.IntegerField(source="direccion.numero")
