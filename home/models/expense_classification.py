from django.contrib.gis.db import models


class ExpenseClassification(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        super(ExpenseClassification, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ExpenseClassification, self).save(*args, **kwargs)