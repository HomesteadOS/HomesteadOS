from graphene_django import DjangoObjectType
from home.models.homestead import Homestead


class HomesteadType(DjangoObjectType):
    class Meta:
        model = Homestead
        fields = ("name", "description", "locations")