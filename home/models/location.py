from django.contrib.gis.db import models

from home.models.homestead import Homestead


class Location(models.Model):
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE, related_name="locations")
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    primary_location = models.BooleanField()

    def __str__(self):
        return self.name
