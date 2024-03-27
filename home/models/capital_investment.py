from decimal import Decimal

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone

from home.models.project import Project


class CapitalInvestment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                                            validators=[MinValueValidator(Decimal('0.01'))])
    investment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project.name

    def clean(self, *args, **kwargs):
        if (self.investment_amount < Decimal('0.01')
                or self.investment_date > timezone.now()):
            raise ValidationError(f"Invalid Capital Investment data. Please check your input. {CapitalInvestment}")
        super(CapitalInvestment, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CapitalInvestment, self).save(*args, **kwargs)