from graphene_django import DjangoObjectType
from home.models import Event


class BudgetType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("start_date", "end_date", "start_time", "end_time", "location", "homestead")