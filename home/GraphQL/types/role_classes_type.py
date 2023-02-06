from graphene_django import DjangoObjectType
from home.models import RoleClasses


class RoleClassesType(DjangoObjectType):
    class Meta:
        model = RoleClasses
        fields = ("name", "description", "enabled")
