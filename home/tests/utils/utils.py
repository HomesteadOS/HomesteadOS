from decimal import Decimal

from django.utils import timezone

from home.models.budget import Budget
from home.models.capital_investment import CapitalInvestment
from home.models.homestead import Homestead
from home.models.location import Location
from home.models.project import Project
from home.models.staff import Staff


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