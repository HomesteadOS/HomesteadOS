from graphene_django import DjangoObjectType
from home.models import CapitalInvestment


class CapitalInvestmentType(DjangoObjectType):
    class Meta:
        model = CapitalInvestment
        fields = ("project", "description")