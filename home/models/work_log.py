from django.contrib.gis.db import models
from django.core.exceptions import ValidationError

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

    def clean(self, *args, **kwargs):
        if self.start_time > self.end_time:
            raise ValidationError(f"Invalid Work Log data. Please check your input. {WorkLog.__str__(self)}")
        super(WorkLog, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(WorkLog, self).save(*args, **kwargs)
