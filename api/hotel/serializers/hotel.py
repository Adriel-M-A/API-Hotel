from rest_framework import serializers
from apps.hotel.models import Hotel

# Importar serializadores del core
from api.core.serializers.ubicacion import UbicacionSerializer
from api.core.serializers.persona import EncargadoSerializer
from api.core.serializers.otro import CategoriaSerializer


class HotelSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer(source="*", read_only=True)
    encargado = EncargadoSerializer()

    class Meta:
        model = Hotel
        fields = ["id", "nombre", "encargado", "ubicacion", "descripcion", "habilitado"]


class HotelMidSerializer(HotelSerializer):
    categoria = CategoriaSerializer()

    class Meta(HotelSerializer.Meta):
        fields = HotelSerializer.Meta.fields + ["categoria"]


class HotelFullSerializer(HotelMidSerializer):
    pass
