from graphene_django import DjangoObjectType
from home.models import Project


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("name", "description", "homestead", "start_date", "due_date", "staff_responsible")