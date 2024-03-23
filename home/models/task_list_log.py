from django.contrib.gis.db import models

from home.models.staff import Staff
from home.models.task_list import TaskList


class TaskListLog(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    comment = models.TextField()

    def __str__(self):
        return self.task_list.name + ' ' + self.staff.first_name + ' ' + self.datetime.__str__()
