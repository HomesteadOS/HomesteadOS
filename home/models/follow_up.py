from django.contrib.gis.db import models

from home.models.homestead import Homestead
from home.models.staff import Staff
from home.models.task import Task


class FollowUp(models.Model):
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    staff_responsible = models.ForeignKey(Staff, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    comment = models.TextField()

    def __str__(self):
        return self.name
