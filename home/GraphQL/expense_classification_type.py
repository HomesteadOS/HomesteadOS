from graphene_django import DjangoObjectType
from home.models import ExpenseClassification


class ExpenseClassificationType(DjangoObjectType):
    class Meta:
        model = ExpenseClassification
        fields = ("name", "description")