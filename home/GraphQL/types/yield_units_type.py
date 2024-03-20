from graphene_django import DjangoObjectType
from home.models import YieldUnits


class YieldUnitsType(DjangoObjectType):
    class Meta:
        model = YieldUnits
        fields = ("name", "abbreviation")
