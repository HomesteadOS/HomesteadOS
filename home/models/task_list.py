from django.contrib.gis.db import models

from home.models.homestead import Homestead
from home.models.staff import Staff
from home.models.task import Task


class TaskList(models.Model):
    homestead = models.ForeignKey(Homestead, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    staff_responsible = models.ForeignKey(Staff, on_delete=models.CASCADE)
    description = models.TextField()
    tasks = models.ManyToManyField(Task)
    due_date = models.DateTimeField()
    start_date = models.DateTimeField()

    def __str__(self):
        return self.name
