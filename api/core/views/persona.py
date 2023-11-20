from rest_framework import viewsets
from apps.core.models import Vendedor, Encargado, Cliente
from api.core.serializers.persona import (
    VendedorSerializer,
    EncargadoSerializer,
    ClienteSerializer,
)


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class EncargadoViewSet(viewsets.ModelViewSet):
    queryset = Encargado.objects.all()
    serializer_class = EncargadoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
