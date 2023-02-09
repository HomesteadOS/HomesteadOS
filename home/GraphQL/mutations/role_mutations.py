import graphene
from home.GraphQL.types.role_type import RoleType
from home.models import Role, RoleClasses


class UpdateRoleMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        email = graphene.String()
        role_class_id = graphene.ID()
        id = graphene.ID()

    role = graphene.Field(RoleType)

    @classmethod
    def mutate(cls, root, info, name, description, primary_location, homestead_id):
        location = Location.objects.get(pk=id)
        save_location(location, description, name, primary_location, homestead_id)

        return UpdateLocationMutation(location=location)


class CreateLocationMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        primary_location = graphene.Boolean()
        homestead_id = graphene.ID()

    location = graphene.Field(LocationType)

    @classmethod
    def mutate(cls, root, info, name, description, primary_location, homestead_id):
        location = Location()
        save_location(location, description, name, primary_location, homestead_id)

        return CreateLocationMutation(location=location)


def save_location(location, description, name, primary_location, homestead_id):
    location.name = name
    location.description = description
    location.primary_location = primary_location
    homestead = Homestead.objects.get(pk=homestead_id)
    location.homestead = homestead
    location.save()
