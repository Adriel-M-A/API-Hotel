from rest_framework import serializers
from apps.core.models import TipoHabitacion, Categoria, Servicio


class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = "__all__"


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"


class CategoriaFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
