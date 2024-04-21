from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

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

    def clean(self, *args, **kwargs):
        if (self.start_time > self.end_time
                or self.end_date < self.start_date
                or self.start_date < timezone.now().date()):
            raise ValidationError(f"Event data. Please check your input. {self}")
        super(Event, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Event, self).save(*args, **kwargs)
