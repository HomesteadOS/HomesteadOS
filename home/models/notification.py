from django.contrib.gis.db import models

from home.models.staff import Staff


class Notification(models.Model):
    message = models.TextField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    scheduled = models.BooleanField(default=False)
    scheduled_datetime = models.DateTimeField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message + ' ' + self.staff.first_name + ' ' + self.datetime.__str__()
