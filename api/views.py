from .models import House
from rest_framework import viewsets
from .serializers import HouseSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all().order_by('title')
    serializer_class = HouseSerializer

