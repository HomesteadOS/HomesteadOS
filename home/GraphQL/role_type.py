from graphene_django import DjangoObjectType
from home.models import Role


class RoleType(DjangoObjectType):
    class Meta:
        model = Role
        fields = ("name", "description", "email", "role_class")
