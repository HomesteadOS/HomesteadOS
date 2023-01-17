import graphene
from graphene_django import DjangoObjectType

from home.models import HomeStead, Location


class HomesteadType(DjangoObjectType):
    class Meta:
        model = HomeStead
        fields = ("name", "description", "locations")


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        fields = ("homestead", "name", "description", "primary_location")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_homesteads = graphene.List(HomesteadType)
    all_locations_by_name = graphene.Field(LocationType, name=graphene.String(required=True))

    def resolve_all_homesteads(root, info):
        return Homestead.objects.select_related("location").all()

    def resolve_locations_by_name(root, info, name):
        try:
            return Location.objects.get(name=name)
        except Location.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

