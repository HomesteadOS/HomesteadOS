from django.contrib.gis.db import models

from home.models.crop import Crop
from home.models.location import Location


class Field(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
