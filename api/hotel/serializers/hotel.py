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

from api.venta.serializers.venta import AlquilerSerializer


# Serializador base y simple para la creacion de un hotel
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id", "nombre", "descripcion"]


# Este serializador es utilizado para dar un listado de todos los hoteles, con su informacion relevante segun el contexto a utilizar
class HotelMidSerializer(HotelSerializer):
    direccion = UbicacionSerializer(source="direccion")
    categoria = CategoriaSerializer(read_only=True)

    class Meta(HotelSerializer.Meta):
        fields = HotelSerializer.Meta.fields


# Este serializador es utilizado para mostrar todos los datos de un hotel, tanto los datos basicos como la serializacion de los datos relacionados con el hotel
# Esta pensado para la pagina de un hotel, donde se muestran todos los datos
class HotelFullSerializer(HotelMidSerializer):
    habitaciones = HabitacionSerializer(many=True, read_only=True)
    encargado = EncargadoSerializer(read_only=True)
    tarifas = PrecioPorTipoSerializer(source="tarifas", many=True, read_only=True)
    paquetes = PaqueteSerializer(many=True, read_only=True)
    descuentos = DescuentoSerializer(many=True, read_only=True)
    temporadas = TemporadaSerializer(many=True, read_only=True)
    alquileres = AlquilerSerializer(many=True, read_only=True, source="alquileres")

    class Meta(HotelMidSerializer.Meta):
        fields = HotelMidSerializer.Meta.fields + [
            "habitaciones",
            "tarifas",
            "paquetes",
            "alquileres",
        ]
