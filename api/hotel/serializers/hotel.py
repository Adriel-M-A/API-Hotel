from rest_framework import serializers
from apps.hotel.models import Hotel, Habitacion, Paquete, Temporada, Descuento

# Importar serializadores del core
from api.core.serializers.ubicacion import UbicacionSerializer
from api.core.serializers.persona import VendedorSerializer, EncargadoSerializer
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
    vendedores = VendedorSerializer(many=True, read_only=True)

    class Meta(HotelMidSerializer.Meta):
        fields = HotelMidSerializer.Meta.fields + ["vendedores"]


# Cosas faltantes para hotel full
# Todo lo que es por disponibilidad nose como hacerlo :P por todos los parametros que se tienen que enviar (minimo fechas inicio y fin)

# Ver cuales paqutes del hotel mostrar (todos o solo disponibles)
# Habitaciones disponibles, enviar una lista de habitaciones o organizarlas segun su tipo o organizarlas desde al front.


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


class DisponibilidadSerializer(serializers.Serializer):
    habitaciones = serializers.PrimaryKeyRelatedField(
        queryset=Habitacion.objects.all(), many=True
    )
    inicio = serializers.DateTimeField()
    fin = serializers.DateTimeField()
    # descuento
    # paquete
    # temporada

    def validate(self, attrs):
        attrs = super().validate(attrs)
        habitaciones = attrs["habitaciones"]
        print(habitaciones)
        # raise ValidationError("No me gusta tu habitacion")
        return attrs

    def create(self, validated_data):
        hotel = validated_data["hotel"]
        habitaciones = validated_data["habitaciones"]
        desde = validated_data["inicio"]
        hasta = validated_data["fin"]
        disponibilidad = hotel.verificar_disponibilidad(habitaciones, desde, hasta)
        return disponibilidad
