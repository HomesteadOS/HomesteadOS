import graphene
from graphene_django import DjangoObjectType

from home.GraphQL.budget_type import BudgetType
from home.GraphQL.captial_investment_type import CapitalInvestmentType
from home.GraphQL.crop_type import CropType
from home.GraphQL.expense_classification_type import ExpenseClassificationType
from home.GraphQL.expense_type import ExpenseType
from home.GraphQL.field_type import FieldType
from home.GraphQL.homestead_type import HomesteadType
from home.GraphQL.location_type import LocationType
from home.GraphQL.project_type import ProjectType
from home.GraphQL.role_classes_type import RoleClassesType
from home.GraphQL.staff_mutations import UpdateStaffMutation, CreateStaffMutation
from home.GraphQL.staff_type import StaffType
from home.GraphQL.supplier_type import SupplierType
from home.GraphQL.role_type import RoleType
from home.GraphQL.yield_units_type import YieldUnitsType
from home.models import Homestead, Location, Staff, Budget, CapitalInvestment, Project, Expense, ExpenseClassification,\
    Supplier, Field, Crop, YieldUnits, RoleClasses, Role


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_homesteads = graphene.List(HomesteadType)
    all_locations = graphene.List(LocationType)
    all_staff = graphene.List(StaffType)
    all_role_classes = graphene.List(RoleClassesType)
    all_roles = graphene.List(RoleType)
    all_crops = graphene.List(CropType)
    all_yield_units = graphene.List(YieldUnitsType)
    all_fields = graphene.List(FieldType)
    all_suppliers = graphene.List(SupplierType)
    all_expense_classifications = graphene.List(ExpenseClassificationType)
    all_expense = graphene.List(ExpenseType)
    all_projects = graphene.List(ProjectType)
    all_capital_investments = graphene.List(CapitalInvestmentType)
    all_budgets = graphene.List(BudgetType)
    all_locations_by_name = graphene.Field(LocationType, name=graphene.String(required=True))
    all_staff_at_homestead_by_name = graphene.List(StaffType, name=graphene.String(required=True))

    def resolve_all_locations(root, info):
        return Location.objects.all()

    def resolve_all_staff(root, info):
        return Staff.objects.all()

    def resolve_all_homesteads(root, info):
        return Homestead.objects.all()

    def resolve_all_role_classes(root, info):
        return RoleClasses.objects.all()

    def resolve_all_crops(root, info):
        return Crop.objects.all()

    def resolve_all_yield_units(root, info):
        return YieldUnits.objects.all()

    def resolve_all_fields(root, info):
        return Field.objects.all()

    def resolve_all_suppliers(root, info):
        return Supplier.objects.all()

    def resolve_all_expense_classifications(root, info):
        return ExpenseClassification.objects.all()

    def resolve_all_expenses(root, info):
        return Expense.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_capital_investments(root, info):
        return CapitalInvestment.objects.all()

    def resolve_all_budgets(root, info):
        return Budget.objects.all()

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


class Mutation(graphene.ObjectType):
    update_staff = UpdateStaffMutation.Field()
    create_staff = CreateStaffMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

