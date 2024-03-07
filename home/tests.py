from datetime import datetime, timedelta

from django.test import TestCase
from home.models import Homestead, Location, Staff, RoleClasses, \
    Role, YieldUnits, Crop, Field, Supplier, Expense, ExpenseClassification, \
    Project, CapitalInvestment, Budget


# Create your tests here.
class HomesteadModelsTest(TestCase):
    def setUp(self) -> None:






    def test_staff_model(self) -> None:
        owner = Staff.objects.get(first_name="Owner")
        odin = Staff.objects.get(first_name="Odin")
        hela = Staff.objects.get(first_name="Hela")
        self.assertEqual(owner.first_name, "Owner")
        self.assertEqual(odin.first_name, "Odin")
        self.assertEqual(hela.first_name, "Hela")
        self.assertEqual(owner.primary_location.name, "Mermaid Of Fire")
        self.assertEqual(odin.primary_location.name, "Corpse Hall")
        self.assertEqual(hela.primary_location.name, "Hel")
        self.assertEqual(owner.last_name, "McOwner")
        self.assertEqual(odin.last_name, "Odinson")
        self.assertEqual(hela.last_name, "Odinson")
        self.assertEqual(owner.email, "owner@mermaidoffire.com")
        self.assertEqual(odin.email, "odin@valhalla.com")
        self.assertEqual(hela.email, "hela@valhalla.com")

    def test_role_and_classes_models(self) -> None:
        owner_class = RoleClasses.objects.get(name="Owner")
        owner_role = Role.objects.get(name="Owner Role")
        self.assertEqual(owner_class.name, "Owner")
        self.assertEqual(owner_role.name, "Owner Role")
        self.assertEqual(owner_class.enabled, True)
        self.assertTrue(owner_role.role_class.enabled, True)

    def test_yield_units_model(self) -> None:
        yu = YieldUnits.objects.get(name="Each")
        self.assertEqual(yu.abbreviation, "ea")

    def test_crop_model(self) -> None:
        crop = Crop.objects.get(name="Tomatoes")
        self.assertEqual(crop.yield_unit.abbreviation, "ea")
        self.assertEqual(crop.name, "Tomatoes")
        self.assertIsNotNone(crop.plant_date)
        self.assertIsNotNone(crop.harvest_date)
        self.assertIsNotNone(crop.harvest_target_date)
        self.assertGreater(crop.yield_actual, 0)
        self.assertGreater(crop.yield_goal, 0)
        self.assertEqual(crop.name, "Tomatoes")
        self.assertIsNotNone(crop.description)

    def test_field_model(self) -> None:
        field = Field.objects.get(name="potato_below_pond")
        self.assertEqual(field.name, "potato_below_pond")
        self.assertEqual(field.crop.name, "Potatoes")
        self.assertEqual(field.location.name, "Fuller Rd")

    def test_supplier_model(self) -> None:
        supplier = Supplier.objects.get(name="Trout r us")
        self.assertIsNotNone(supplier.location)

    def test_expense_classification_model(self) -> None:
        ex_class_1 = ExpenseClassification.objects.get(name="Input")
        ex_class_2 = ExpenseClassification.objects.get(name="Seed")
        ex_class_3 = ExpenseClassification.objects.get(name="Mortgage")
        self.assertIsNotNone(ex_class_1.description)
        self.assertIsNotNone(ex_class_2.description)
        self.assertIsNotNone(ex_class_3.description)

    def test_expense_model(self) -> None:
        expense_1 = Expense.objects.get(description="Buying cold stuff")
        expense_2 = Expense.objects.get(description="Buying stuff")
        expense_3 = Expense.objects.get(description="Paying for Valhalla")
        self.assertEqual(expense_1.approved, True)
        self.assertEqual(expense_2.approved, True)
        self.assertEqual(expense_3.approved, True)
        self.assertGreater(expense_1.amount, 0)
        self.assertGreater(expense_2.amount, 0)
        self.assertGreater(expense_3.amount, 0)
        self.assertGreater(expense_1.debt, 0)
        self.assertGreater(expense_2.debt, 0)
        self.assertGreater(expense_3.debt, 0)
        self.assertIsNotNone(expense_1.spender)
        self.assertIsNotNone(expense_2.spender)
        self.assertIsNotNone(expense_3.spender)
        self.assertIsNotNone(expense_1.debtor)
        self.assertIsNotNone(expense_2.debtor)
        self.assertIsNotNone(expense_3.debtor)
        self.assertIsNotNone(expense_1.classification)
        self.assertIsNotNone(expense_2.classification)
        self.assertIsNotNone(expense_3.classification)
        self.assertIsNotNone(expense_1.supplier)
        self.assertIsNotNone(expense_2.supplier)
        self.assertIsNotNone(expense_3.supplier)
        self.assertIsNotNone(expense_1.datetime)
        self.assertIsNotNone(expense_2.datetime)
        self.assertIsNotNone(expense_3.datetime)
        self.assertGreater(expense_1.percent, 10)
        self.assertGreater(expense_2.percent, 10)
        self.assertGreater(expense_3.percent, 10)
