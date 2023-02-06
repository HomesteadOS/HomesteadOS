import graphene
from home.GraphQL.types.staff_type import StaffType
from home.models import Staff, Location


class UpdateStaffMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        primary_location = graphene.ID()
        id = graphene.ID()

    staff = graphene.Field(StaffType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, primary_location):
        staff = Staff.objects.get(pk=id)
        staff.first_name = first_name
        staff.last_name = last_name
        staff.email = email
        new_location = Location.objects.get(pk=primary_location)
        staff.primary_location = new_location
        staff.save()

        return UpdateStaffMutation(staff=staff)


class CreateStaffMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        primary_location = graphene.ID()

    staff = graphene.Field(StaffType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, primary_location):
        staff = Staff()
        staff.first_name = first_name
        staff.last_name = last_name
        staff.email = email
        new_location = Location.objects.get(pk=primary_location)
        staff.primary_location = new_location
        staff.save()

        return CreateStaffMutation(staff=staff)