from rest_framework import viewsets
from apps.hotel.models import Hotel

from api.hotel.serializers.hotel import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
