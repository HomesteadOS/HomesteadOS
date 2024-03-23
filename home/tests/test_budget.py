import pytest
from django.utils import timezone
from home.models.budget import Budget
from home.models.capital_investment import CapitalInvestment


def test_budget_creation_with_valid_data():
    capital_investment = CapitalInvestment.objects.create(name="Test Investment")
    budget = Budget.objects.create(
        property_cost=100000.00,
        property_cost_monthly=8333.33,
        salary=5000.00,
        capital_investment=[capital_investment],
        period_start=timezone.now(),
        period_end=timezone.now() + timezone.timedelta(days=30)
    )
    assert budget is not None


def test_budget_string_representation():
    capital_investment = CapitalInvestment.objects.create(name="Test Investment")
    budget = Budget.objects.create(
        property_cost=100000.00,
        property_cost_monthly=8333.33,
        salary=5000.00,
        capital_investment=[capital_investment],
        period_start=timezone.now(),
        period_end=timezone.now() + timezone.timedelta(days=30)
    )
    assert str(budget) == f"{budget.period_start}-{budget.period_end}"


def test_budget_with_negative_property_cost():
    with pytest.raises(ValueError):
        capital_investment = CapitalInvestment.objects.create(name="Test Investment")
        Budget.objects.create(
            property_cost=-100000.00,
            property_cost_monthly=8333.33,
            salary=5000.00,
            capital_investment=[capital_investment],
            period_start=timezone.now(),
            period_end=timezone.now() + timezone.timedelta(days=30)
        )


def test_budget_with_negative_salary():
    with pytest.raises(ValueError):
        capital_investment = CapitalInvestment.objects.create(name="Test Investment")
        Budget.objects.create(
            property_cost=100000.00,
            property_cost_monthly=8333.33,
            salary=-5000.00,
            capital_investment=[capital_investment],
            period_start=timezone.now(),
            period_end=timezone.now() + timezone.timedelta(days=30)
        )


def test_budget_with_end_date_before_start_date():
    with pytest.raises(ValueError):
        capital_investment = CapitalInvestment.objects.create(name="Test Investment")
        Budget.objects.create(
            property_cost=100000.00,
            property_cost_monthly=8333.33,
            salary=5000.00,
            capital_investment=[capital_investment],
            period_start=timezone.now(),
            period_end=timezone.now() - timezone.timedelta(days=30)
        )
