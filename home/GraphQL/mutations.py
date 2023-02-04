import graphene

from home.GraphQL.staff_mutations import UpdateStaffMutation, CreateStaffMutation


class Mutation(graphene.ObjectType):
    update_staff = UpdateStaffMutation.Field()
    create_staff = CreateStaffMutation.Field()
