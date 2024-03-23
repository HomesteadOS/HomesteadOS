from django.contrib.gis.db import models

from home.models.location import Location


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    primary_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
