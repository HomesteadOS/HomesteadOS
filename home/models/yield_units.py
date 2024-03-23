from django.contrib.gis.db import models


class YieldUnits(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.name
