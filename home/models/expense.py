from decimal import Decimal

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from home.models.expense_classification import ExpenseClassification
from home.models.staff import Staff
from home.models.supplier import Supplier


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    spender = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='spender')
    debtor = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='debtor')
    datetime = models.DateTimeField()
    description = models.TextField()
    percent = models.IntegerField()
    classification = models.ForeignKey(ExpenseClassification, on_delete=models.DO_NOTHING)
    classification_detail = models.TextField()
    paid_external = models.BooleanField()
    paid_internal = models.BooleanField()
    approved = models.BooleanField(default=True)
    store = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.spender.last_name + ', ' + self.spender.first_name + ' spent on ' + self.datetime.__str__() + ' ' \
            + self.debtor.last_name + ', ' + self.debtor.first_name + ' owes ' + self.debt.__str__()

    def clean(self, *args, **kwargs):
        if (self.amount < Decimal('0.00')
                or self.debt <= Decimal('0.00')
                or self.datetime > timezone.now()):
            raise ValidationError(f"Expense data. Please check your input. {self}")
        super(Expense, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Expense, self).save(*args, **kwargs)
