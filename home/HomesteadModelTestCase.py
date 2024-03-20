from datetime import datetime, timedelta

from django.test import TestCase

from home.models import Homestead, Location, Staff, RoleClasses, \
    Role, YieldUnits, Crop, Field, Supplier, Expense, ExpenseClassification, \
    Project, CapitalInvestment, Budget


class HomesteadModelTestCase(TestCase):
    def __init__(self):
        super().__init__()
        self.mermaid = Homestead()
        self.valhalla = Homestead()
        self.fuller = Location()
        self.corpse_hall = Location()
        self.hel = Location()
        self.owner = Staff()
        self.odin = Staff()
        self.hela = Staff()
        self.owner_class = RoleClasses()
        self.owner_role = Role()
        self.yield_unit = YieldUnits()
        self.crop = Crop()
        self.field1 = Field()
        self.supplier = Supplier()
        self.expense_class1 = ExpenseClassification()
        self.expense_class2 = ExpenseClassification()
        self.expense_class3 = ExpenseClassification()
        self.expense1 = Expense()
        self.expense2 = Expense()
        self.expense3 = Expense()
        self.project = Project()
        self.cap_investment = CapitalInvestment()
        self.cap_investment2 = CapitalInvestment()
        self.cap_investment3 = CapitalInvestment()
        self.budget = Budget()
        self.test_data_setup()

    def test_data_setup(self) -> None:
        self.mermaid = Homestead.objects.create(name="Mermaid Of Fire",
                                                description="The one, the only, the MERMAID OF FIRE")
        self.valhalla = Homestead.objects.create(name="Valhalla", description="Feast, Fight, ...")
        self.fuller = Location.objects.create(name="Fuller Rd", description="The Easton location", primary_location=True,
                                              homestead=self.mermaid)
        self.corpse_hall = Location.objects.create(name="Corpse Hall", description="Odin's hall", primary_location=True,
                                                   homestead=self.valhalla)
        self.hel = Location.objects.create(name="Hel", description="Cold as Hel", primary_location=False,
                                           homestead=self.valhalla)
        self.owner = Staff.objects.create(first_name="Owner", last_name="McOwner", email="owner@mermaidoffire.com",
                                          primary_location=self.fuller)
        self.odin = Staff.objects.create(first_name="Odin", last_name="Odinson", email="odin@valhalla.com",
                                         primary_location=self.corpse_hall)
        self.hela = Staff.objects.create(first_name="Hela", last_name="Odinson", email="hela@valhalla.com",
                                         primary_location=self.hel)
        self.owner_class = RoleClasses.objects.create(name="Owner", description="Owner role class", enabled=True)
        self.owner_role = Role.objects.create(name="Owner Role", description="The Owner Role",
                                              email="owner@mermaidoffire.com", role_class=self.owner_class)
        self.yield_unit = YieldUnits.objects.create(name="Each", abbreviation="ea")
        self.crop = Crop.objects.create(name="Potatoes",
                                        description="Red Potatoes",
                                        plant_date=datetime.now(),
                                        harvest_date=datetime.now() + timedelta(days=31),
                                        harvest_target_date=datetime.now() + timedelta(days=28),
                                        yield_goal=30,
                                        yield_unit=self.yield_unit,
                                        yield_actual=25)
        self.field1 = Field.objects.create(name="potato_below_pond",
                                           location=self.fuller,
                                           crop=self.crop)
        self.supplier = Supplier.objects.create(name="Trout r us",
                                                description="Trout pond stocking",
                                                location=self.fuller)
        self.expense_class_1 = ExpenseClassification.objects.create(name="Input",
                                                                    description="Inputs")
        self.expense_class_2 = ExpenseClassification.objects.create(name="Seed",
                                                                    description="Seeds")
        self.expense_class_3 = ExpenseClassification.objects.create(name="Mortgage",
                                                                    description="Gotta pay the bank")
        self.expense_1 = Expense.objects.create(approved=True,
                                                amount=550.00,
                                                debt=100.00,
                                                spender=self.owner,
                                                debtor=self.hela,
                                                datetime=datetime.now(),
                                                description="Buying cold stuff",
                                                percent=25,
                                                classification=self.expense_class_1,
                                                classification_detail="Buying all teh cold as hel things",
                                                paid_external=True,
                                                paid_internal=False,
                                                store="Thing n stuff",
                                                supplier=self.supplier)
        self.expense_2 = Expense.objects.create(approved=True,
                                                amount=350.00,
                                                debt=200.00,
                                                spender=self.owner,
                                                debtor=self.odin,
                                                datetime=datetime.now(),
                                                description="Buying stuff",
                                                percent=25,
                                                classification=self.expense_class_2,
                                                classification_detail="Buying all teh things",
                                                paid_external=True,
                                                paid_internal=False,
                                                store="Thing n stuff",
                                                supplier=self.supplier)
        self.expense_3 = Expense.objects.create(approved=True,
                                                amount=3500.00,
                                                debt=2000.00,
                                                spender=self.odin,
                                                debtor=self.hela,
                                                datetime=datetime.now(),
                                                description="Paying for Valhalla",
                                                percent=25,
                                                classification=self.expense_class_3,
                                                classification_detail="Bank gets Bank",
                                                paid_external=False,
                                                paid_internal=True,
                                                store="Bank of Asgard",
                                                supplier=self.supplier)
        self.project = Project.objects.create(name="Stock the pond",
                                              description="Trout in the pond",
                                              homestead=self.mermaid,
                                              start_date=datetime.now(),
                                              due_date=datetime.now(),
                                              staff_responsible=self.owner)
        self.cap_investment = CapitalInvestment.objects.create(project=self.project,
                                                               description="Buying fish and water")
        self.cap_investment_2 = CapitalInvestment.objects.create(project=self.project,
                                                                 description="Buying oxygen pump")
        self.cap_investment_3 = CapitalInvestment.objects.create(project=self.project,
                                                                 description="Water pumps")
        self.budget = Budget.objects.create(property_cost=500000.00,
                                            property_cost_monthly=5000.00,
                                            salary=1000.00,
                                            period_start=datetime.now(),
                                            period_end=datetime.now() + timedelta(days=31))
        self.budget.capital_investment.add(self.cap_investment)
        self.budget.capital_investment.add(self.cap_investment_2)
        self.budget.capital_investment.add(self.cap_investment_3)

