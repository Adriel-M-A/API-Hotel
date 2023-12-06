from rest_framework import viewsets
from apps.core.models import TipoHabitacion, Servicio, Categoria
from api.core.serializers.otro import (
    TipoHabitacionSerializer,
    ServicioSerializer,
    CategoriaSerializer,
)


class TipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
