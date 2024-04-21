from django.contrib.gis.db import models

from home.models.event import Event
from home.models.expense import Expense


class EventExpense(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    planned = models.BooleanField(default=False)

    def __str__(self):
        return self.event.__str__() + ' ' + self.expense.__str__()

    def clean(self, *args, **kwargs):
        super(EventExpense, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(EventExpense, self).save(*args, **kwargs)
