from django.contrib.gis.db import models

from home.models.staff import Staff
from home.models.task import Task


class WorkLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    comment = models.TextField()

    def __str__(self):
        return self.task.name + ' ' + self.staff.first_name + ' ' + self.start_time.__str__() + ' ' + self.end_time.__str__()
