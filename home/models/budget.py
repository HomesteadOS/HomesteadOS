from django.contrib.gis.db import models

from home.models.capital_investment import CapitalInvestment


class Budget(models.Model):
    property_cost = models.DecimalField(max_digits=10, decimal_places=2)
    property_cost_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    capital_investment = models.ManyToManyField(CapitalInvestment, related_name='investments')
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()

    def __str__(self):
        return self.period_start.__str__() + '-' + self.period_end.__str__()
