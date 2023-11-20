from rest_framework import serializers
from apps.core.models import TipoHabitacion, Categoria, Servicio


class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = "__all__"


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ["nombre", "descripcion"]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion", "estrellas"]


class CategoriaMidSerializer(CategoriaSerializer):
    servicios = ServicioSerializer(many=True, read_only=True)

    class Meta(CategoriaSerializer.Meta):
        fields = CategoriaSerializer.Meta.fields + ["servicios"]
