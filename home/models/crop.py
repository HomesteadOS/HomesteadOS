from django.contrib.gis.db import models

from home.models.yield_units import YieldUnits


class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plant_date = models.DateTimeField()
    harvest_date = models.DateTimeField()
    harvest_target_date = models.DateTimeField()
    yield_goal = models.IntegerField()
    yield_unit = models.ForeignKey(YieldUnits, on_delete=models.PROTECT)
    yield_actual = models.IntegerField()

    def __str__(self):
        return self.name
