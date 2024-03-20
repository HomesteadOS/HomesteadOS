from graphene_django import DjangoObjectType
from home.models import Location


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        fields = ("homestead", "name", "description", "primary_location")