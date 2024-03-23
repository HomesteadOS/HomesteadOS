import graphene
from home.GraphQL.types.homestead_type import HomesteadType
from home.models.homestead import Homestead


class UpdateHomesteadMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        id = graphene.ID()

    homestead = graphene.Field(HomesteadType)

    @classmethod
    def mutate(cls, root, info, name, description,):
        homestead = Homestead.objects.get(pk=id)
        save_homestead(homestead, description, name)

        return UpdateHomesteadMutation(homestead=homestead)


class CreateHomesteadMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    homestead = graphene.Field(HomesteadType)

    @classmethod
    def mutate(cls, root, info, name, description):
        homestead = Homestead()
        save_homestead(homestead, description, name)

        return CreateHomesteadMutation(homestead=homestead)


def save_homestead(homestead, description, name):
    homestead.name = name
    homestead.description = description
    homestead.save()
