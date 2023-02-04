import graphene
from graphene_django import DjangoObjectType

from home.models import Homestead, Location, Staff


class HomesteadType(DjangoObjectType):
    class Meta:
        model = Homestead
        fields = ("name", "description", "locations")


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        fields = ("homestead", "name", "description", "primary_location")


class StaffType(DjangoObjectType):
    class Meta:
        model = Staff
        fields = ("first_name", "last_name", "email", "primary_location")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_homesteads = graphene.List(HomesteadType)
    all_locations_by_name = graphene.Field(LocationType, name=graphene.String(required=True))
    all_staff_at_homestead_by_name = graphene.List(StaffType, name=graphene.String(required=True))

    def resolve_all_homesteads(root, info):
        return Homestead.objects.all()

    def resolve_locations_by_name(root, info, name):
        try:
            return Location.objects.get(name=name)
        except Location.DoesNotExist:
            return None

    def resolve_staff_at_homestead_by_name(root, info, name):
        try:
            return Staff.objects.fitler(homestead__name=name)
        except Staff.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

