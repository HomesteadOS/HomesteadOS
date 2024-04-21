from django.contrib.gis.db import models

from home.models.homestead import Homestead
from home.models.location import Location
from home.models.staff import Staff


class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    homestead = models.ForeignKey(Homestead, on_delete=models.DO_NOTHING)
    staff_responsible = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.start_date.__str__() + ' ' + self.start_time.__str__() + ' ' + self.location.name + ' @ ' + self.homestead.name
