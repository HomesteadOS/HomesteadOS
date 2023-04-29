from datetime import datetime, timedelta

from django.test import TestCase
from home.models import Homestead, Location, Staff, RoleClasses, \
    Role, YieldUnits, Crop, Field, Supplier, Expense, ExpenseClassification, \
    Project, CapitalInvestment, Budget


# Create your tests here.
class HomesteadModelsTest(TestCase):
    def setUp(self) -> None:
        mermaid = Homestead.objects.create(name="Mermaid Of Fire", description="The one, the only, the MERMAID OF FIRE")
        valhalla = Homestead.objects.create(name="Valhalla", description="Feast, Fight, ...")
        fuller = Location.objects.create(name="Fuller Rd", description="The Easton location", primary_location=True,
                                         homestead=mermaid)
        corpse_hall = Location.objects.create(name="Corpse Hall", description="Odin's hall", primary_location=True,
                                              homestead=valhalla)
        hel = Location.objects.create(name="Hel", description="Cold as Hel", primary_location=False, homestead=valhalla)
        owner = Staff.objects.create(first_name="Owner", last_name="McOwner", email="owner@mermaidoffire.com",
                                     primary_location=fuller)
        odin = Staff.objects.create(first_name="Odin", last_name="Odinson", email="odin@valhalla.com",
                                    primary_location=corpse_hall)
        hela = Staff.objects.create(first_name="Hela", last_name="Odinson", email="hela@valhalla.com",
                                    primary_location=hel)
        owner_class = RoleClasses.objects.create(name="Owner", description="Owner role class", enabled=True)
        owner_role = Role.objects.create(name="Owner Role", description="The Owner Role",
                                         email="owner@mermaidoffire.com", role_class=owner_class)
        yield_unit = YieldUnits.objects.create(name="Each", abbreviation="ea")
        crop = Crop.objects.create(name="Potatoes",
                                   description="Red Potatoes",
                                   plant_date=datetime.now(),
                                   harvest_date=datetime.now() + timedelta(days=31),
                                   harvest_target_date=datetime.now() + timedelta(days=28),
                                   yield_goal=30,
                                   yield_unit=yield_unit,
                                   yield_actual=25)
        field1 = Field.objects.create(name="potato_below_pond",
                                      location=fuller,
                                      crop=crop)
        supplier = Supplier.objects.create(name="Trout r us",
                                           description="Trout pond stocking",
                                           location=fuller)
        expense_class_1 = ExpenseClassification.objects.create(name="Input",
                                                               description="Inputs")
        expense_class_2 = ExpenseClassification.objects.create(name="Seed",
                                                               description="Seeds")
        expense_class_3 = ExpenseClassification.objects.create(name="Mortgage",
                                                               description="Gotta pay the bank")
        expense_1 = Expense.objects.create(approved=True,
                                           amount=550.00,
                                           debt=100.00,
                                           spender=owner,
                                           debtor=hela,
                                           datetime=datetime.now(),
                                           description="Buying cold stuff",
                                           percent=25,
                                           classification=expense_class_1,
                                           classification_detail="Buying all teh cold as hel things",
                                           paid_external=True,
                                           paid_internal=False,
                                           store="Thing n stuff",
                                           supplier=supplier)
        expense_2 = Expense.objects.create(approved=True,
                                           amount=350.00,
                                           debt=200.00,
                                           spender=owner,
                                           debtor=odin,
                                           datetime=datetime.now(),
                                           description="Buying stuff",
                                           percent=25,
                                           classification=expense_class_2,
                                           classification_detail="Buying all teh things",
                                           paid_external=True,
                                           paid_internal=False,
                                           store="Thing n stuff",
                                           supplier=supplier)
        expense_3 = Expense.objects.create(approved=True,
                                           amount=3500.00,
                                           debt=2000.00,
                                           spender=odin,
                                           debtor=hela,
                                           datetime=datetime.now(),
                                           description="Paying for Valhalla",
                                           percent=25,
                                           classification=expense_class_3,
                                           classification_detail="Bank gets Bank",
                                           paid_external=False,
                                           paid_internal=True,
                                           store="Bank of Asgard",
                                           supplier=supplier)
        project = Project.objects.create(name="Stock the pond",
                                         description="Trout in the pond",
                                         homestead=mermaid,
                                         start_date=datetime.now(),
                                         due_date=datetime.now(),
                                         staff_responsible=owner)
        cap_investment = CapitalInvestment.objects.create(project=project,
                                                          description="Buying fish and water")
        cap_investment_2 = CapitalInvestment.objects.create(project=project,
                                                            description="Buying oxygen pump")
        cap_investment_3 = CapitalInvestment.objects.create(project=project,
                                                            description="Water pumps")
        budget = Budget.objects.create(property_cost=500000.00,
                                       property_cost_monthly=5000.00,
                                       salary=1000.00,
                                       period_start=datetime.now(),
                                       period_end=datetime.now() + timedelta(days=31))
        budget.capital_investment.add(cap_investment)
        budget.capital_investment.add(cap_investment_2)
        budget.capital_investment.add(cap_investment_3)

    def test_homestead_models(self) -> None:
        mermaid = Homestead.objects.get(name="Mermaid Of Fire")
        valhalla = Homestead.objects.get(name="Valhalla")
        self.assertEqual(mermaid.name, "Mermaid Of Fire")
        self.assertEqual(valhalla.name, "Valhalla")

    def test_location_models(self) -> None:
        fuller = Location.objects.get(name="Fuller Rd")
        corpse_hall = Location.objects.get(name="Corpse Hall")
        hel = Location.objects.get(name="Hel")
        self.assertEqual(fuller.name, "Fuller Rd")
        self.assertEqual(corpse_hall.name, "Corpse Hall")
        self.assertEqual(hel.name, "Hel")
        self.assertEqual(fuller.primary_location, True)
        self.assertEqual(corpse_hall.primary_location, True)
        self.assertEqual(hel.primary_location, False)
        self.assertIsNotNone(fuller.description)
        self.assertIsNotNone(corpse_hall.description)
        self.assertIsNotNone(hel.description)

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
