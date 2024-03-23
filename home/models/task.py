from django.contrib.gis.db import models

from home.models.homestead import Homestead
from home.models.staff import Staff


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE)
    staff_responsible = models.ForeignKey(Staff, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    comment = models.TextField()

    def __str__(self):
        return self.name
