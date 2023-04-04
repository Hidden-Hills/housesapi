from django.db import models

class House(models.Model):
    title = models.CharField(max_length=100000, default=False)
    price = models.CharField(max_length=100000, default=False)
    bedRooms = models.CharField(max_length=100000, default=False)
    bathRooms = models.CharField(max_length=100000, default=False)
    location = models.CharField(max_length=100000, default=False)
    maxGuests = models.CharField(max_length=100000, default=False)
    description = models.CharField(max_length=100000, default=False)
    ratings = models.FloatField(max_length=100000, default=False)
    reviews = models.CharField(max_length=100000, default=False)

    def __int__(self):
        return self.title


