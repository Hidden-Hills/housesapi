from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ['title', 'price', 'bedRooms', 'bathRooms', 'location', 'maxGuests', 'description', 'ratings', 'reviews']
