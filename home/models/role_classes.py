from django.contrib.gis.db import models


class RoleClasses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    enabled = models.BooleanField()

    def __str__(self):
        return self.name
