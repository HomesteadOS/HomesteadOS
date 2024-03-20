from graphene_django import DjangoObjectType
from home.models import Expense


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense
        fields = ("amount", "debt", "spender", "debtor", "datetime", "description", "percent", "classification",\
                  "classification_detail", "paid_external", "paid_internal", "approved", "store", "supplier")