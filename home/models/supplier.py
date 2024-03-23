from django.contrib.gis.db import models

from home.models.location import Location


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
