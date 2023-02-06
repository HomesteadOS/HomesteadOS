from graphene_django import DjangoObjectType
from home.models import Supplier


class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier
        fields = ("name", "description", "location")