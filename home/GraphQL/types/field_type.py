from graphene_django import DjangoObjectType
from home.models import Field


class FieldType(DjangoObjectType):
    class Meta:
        model = Field
        fields = ("location", "crop", "name")