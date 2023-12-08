from rest_framework import serializers
from apps.hotel.models import Hotel

# Importar serializadores del core
from api.core.serializers.ubicacion import UbicacionSerializer
from api.core.serializers.persona import EncargadoSerializer
from api.core.serializers.otros import CategoriaSerializer

from api.hotel.serializers.otros import (
    HabitacionSerializer,
    PaqueteSerializer,
    TemporadaSerializer,
    DescuentoSerializer,
    PrecioPorTipoSerializer,
)


# Serializador base y simple para la creacion de un hotel
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


# Este serializador es utilizado para dar un listado de todos los hoteles, con su informacion relevante segun el contexto a utilizar
class HotelMidSerializer(HotelSerializer):
    direccion = UbicacionSerializer(source="direccion")
    categoria = CategoriaSerializer(read_only=True)

    class Meta(HotelSerializer.Meta):
        fields = HotelSerializer.Meta.fields


# Este serializador es utilizado para mostrar todos los datos de un hotel, tanto los datos basico como la serializacion de los datos relacionados con el hotel
class HotelFullSerializer(HotelMidSerializer):
    habitaciones = HabitacionSerializer(many=True, read_only=True)
    encargado = EncargadoSerializer(read_only=True)
    tarifas = PrecioPorTipoSerializer(source="tarifas", many=True, read_only=True)
    paquetes = PaqueteSerializer(many=True, read_only=True)
    descuentos = DescuentoSerializer(many=True, read_only=True)
    temporadas = TemporadaSerializer(many=True, read_only=True)

    class Meta(HotelMidSerializer.Meta):
        fields = HotelMidSerializer.Meta.fields + [
            "habitaciones",
            "tarifas",
            "paquetes",
            "descuentos",
            "temporadas",
        ]
