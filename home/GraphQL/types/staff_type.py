from home.models import Staff
from graphene_django import DjangoObjectType

class StaffType(DjangoObjectType):
    class Meta:
        model = Staff
        fields = ("first_name", "last_name", "email", "primary_location")
