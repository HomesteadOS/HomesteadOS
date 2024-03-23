from django.contrib.gis.db import models

from home.models.project import Project


class CapitalInvestment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.project.name
