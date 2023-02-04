import graphene
from graphene_django import DjangoObjectType

from home.models import Homestead, Location, Staff, Budget, CapitalInvestment, Project, Expense, ExpenseClassification,\
    Supplier, Field, Crop, YieldUnits, RoleClasses, Role


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


class BudgetType(DjangoObjectType):
    class Meta:
        model = Budget
        fields = ("property_cost", "property_cost_monthly", "salary", "capital_investment", "period_start",\
                  "period_end")


class CapitalInvestmentType(DjangoObjectType):
    class Meta:
        model = CapitalInvestment
        fields = ("project", "description")


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("name", "description", "homestead", "start_date", "due_date", "staff_responsible")


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense
        fields = ("amount", "debt", "spender", "debtor", "datetime", "description", "percent", "classification",\
                  "classification_detail", "paid_external", "paid_internal", "approved", "store", "supplier")


class ExpenseClassificationType(DjangoObjectType):
    class Meta:
        model = ExpenseClassification
        fields = ("name", "description")


class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier
        fields = ("name", "description", "location")


class FieldType(DjangoObjectType):
    class Meta:
        model = Field
        fields = ("location", "crop", "name")


class CropType(DjangoObjectType):
    class Meta:
        model = Crop
        fields = ("name", "description", "plant_date", "harvest_date", "harvest_target_date", "yield_goal", \
                  "yield_unit", "yield_actual")


class YieldUnitsType(DjangoObjectType):
    class Meta:
        model = YieldUnits
        fields = ("name", "abbreviation")


class RoleClassesType(DjangoObjectType):
    class Meta:
        model = RoleClasses
        fields = ("name", "description", "enabled")


class RoleType(DjangoObjectType):
    class Meta:
        model = Role
        fields = ("name", "description", "email", "role_class")

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


schema = graphene.Schema(query=Query)

