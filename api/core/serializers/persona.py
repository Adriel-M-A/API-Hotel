from rest_framework import serializers
from apps.core.models import Persona, Vendedor, Encargado, Cliente


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"


class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
