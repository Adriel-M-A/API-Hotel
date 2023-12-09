from rest_framework import serializers
from apps.core.models import TipoDocumento, Persona, Vendedor, Encargado, Cliente


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ["nombre"]


class PersonaSerializer(serializers.ModelSerializer):
    tipo_documento = serializers.CharField(source="tipo_documento.nombre")

    class Meta:
        model = Persona
        fields = "__all__"


class VendedorSerializer(PersonaSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"


class EncargadoSerializer(PersonaSerializer):
    class Meta:
        model = Encargado
        fields = "__all__"


class ClienteSerializer(PersonaSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
