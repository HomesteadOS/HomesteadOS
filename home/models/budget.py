from decimal import Decimal

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from home.models.capital_investment import CapitalInvestment


class Budget(models.Model):
    property_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                        validators=[MinValueValidator(Decimal('0.01'))])
    property_cost_monthly = models.DecimalField(max_digits=10, decimal_places=2
                                                , validators=[MinValueValidator(Decimal('0.01'))])
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    capital_investment = models.ManyToManyField(CapitalInvestment, related_name='investments')
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()

    def __str__(self):
        return self.period_start.__str__() + '-' + self.period_end.__str__()

    def clean(self, *args, **kwargs):
        if (self.property_cost < Decimal('0.01')
                or self.property_cost_monthly < Decimal('0.01')
                or self.salary < Decimal('0.01')
                or self.period_start > self.period_end):
            raise ValidationError(f"Invalid budget data. Please check your input. {Budget}")
        super(Budget, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Budget, self).save(*args, **kwargs)
