from decimal import Decimal

from django.utils import timezone

from home.models.budget import Budget
from home.models.capital_investment import CapitalInvestment
from home.models.crop import Crop
from home.models.event import Event
from home.models.event_expense import EventExpense
from home.models.expense import Expense
from home.models.expense_classification import ExpenseClassification
from home.models.homestead import Homestead
from home.models.location import Location
from home.models.project import Project
from home.models.staff import Staff
from home.models.supplier import Supplier
from home.models.yield_units import YieldUnits


def set_up(self=None):
    self.homestead = Homestead.objects.create(name="Test Homestead", description="Test Description")
    self.location = Location.objects.create(name="Test Location", description="Test Description",
                                            homestead=self.homestead, primary_location=True)
    self.staff = Staff.objects.create(first_name="Test", last_name="Staff", email="test@homesteados.org"
                                      , primary_location=self.location)
    self.project = Project.objects.create(name="Test Project", description="Test Description",
                                          start_date=timezone.now(), due_date=timezone.now()
                                          , staff_responsible=self.staff, homestead=self.homestead)
    self.capital_investment = CapitalInvestment.objects.create(project=self.project, description="Test Description",
                                                               investment_amount=Decimal("10000.00"),
                                                               investment_date=timezone.now())
    self.budget = Budget.objects.create(
        property_cost=Decimal("100000.00"),
        property_cost_monthly=Decimal("8888.33"),
        salary=Decimal("5000.00"),
        period_start=timezone.now(),
        period_end=timezone.now() + timezone.timedelta(days=30)
    )
    self.capital_investment.budget = self.budget
    self.capital_investment.save()
    self.supplier = Supplier.objects.create(name='Test Supplier', description='Test Description', location=self.location)
    self.expense_classification = ExpenseClassification.objects.create(name='Test Classification', description='Test '
                                                                                                               'Description')
    self.expense = Expense.objects.create(
        amount=Decimal('100.00'),
        debt=Decimal('50.00'),
        spender=self.staff,
        debtor=self.staff,
        datetime=timezone.now(),
        description='Test Description',
        percent=50,
        classification=self.expense_classification,
        classification_detail='Test Classification Detail',
        paid_external=False,
        paid_internal=False,
        approved=True,
        store='Test Store',
        supplier=self.supplier
    )
    self.event = Event.objects.create(
        start_date=timezone.now().date(),
        end_date=(timezone.now() + timezone.timedelta(days=1)).date(),
        start_time=timezone.now().time(),
        end_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
        location=self.location,
        homestead=self.homestead,
        staff_responsible=self.staff
    )
    self.event_expense = EventExpense.objects.create(expense=self.expense, event=self.event)
    self.yield_unit = YieldUnits.objects.create(name="Test Unit")
    self.crop = Crop.objects.create(
        name="Test Crop",
        description="Test Description",
        plant_date=timezone.now() + timezone.timedelta(days=10),
        harvest_date=timezone.now() + timezone.timedelta(days=90),
        harvest_target_date=timezone.now() + timezone.timedelta(days=80),
        yield_goal=Decimal('1000.00'),
        yield_unit=self.yield_unit,
        yield_actual=Decimal('900.00')
    )
