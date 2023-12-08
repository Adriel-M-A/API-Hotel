from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from rest_framework.exceptions import NotFound

from apps.hotel.models import Hotel

from api.hotel.serializers.hotel import (
    HotelSerializer,
    HotelMidSerializer,
    HotelFullSerializer,
)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=False, url_path="mid")
    def mid(self, request):
        hoteles = Hotel.objects.all()
        serializer = HotelMidSerializer(hoteles, many=True)
        return Response(serializer.data)

    @action(detail=True, url_path="full")
    def full(self, request, pk=None):
        try:
            hotel = self.get_object()
        except Http404:
            raise NotFound(detail="Hotel no encontrado", code=404)

        serializer = HotelFullSerializer(hotel)
        return Response(serializer.data)
