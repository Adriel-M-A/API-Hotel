from rest_framework import serializers
from apps.hotel.models import Hotel

# Importar serializadores del core
from api.core.serializers.ubicacion import UbicacionSerializer
from api.core.serializers.persona import EncargadoSerializer
from api.core.serializers.otro import CategoriaSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class HotelMidSerializer(HotelSerializer):
    direccion = UbicacionSerializer(source="direccion")
    categoria = CategoriaSerializer(read_only=True)

    class Meta(HotelSerializer.Meta):
        fields = HotelSerializer.Meta.fields


class HotelFullSerializer(HotelMidSerializer):
    pass
