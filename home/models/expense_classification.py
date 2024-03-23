from django.contrib.gis.db import models


class ExpenseClassification(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
