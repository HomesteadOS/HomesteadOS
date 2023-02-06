from graphene_django import DjangoObjectType
from home.models import Budget


class BudgetType(DjangoObjectType):
    class Meta:
        model = Budget
        fields = ("property_cost", "property_cost_monthly", "salary", "capital_investment", "period_start",\
                  "period_end")