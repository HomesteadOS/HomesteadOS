from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from home.models.budget import Budget
from home.tests.utils import utils


class BudgetTestCase(TestCase):
    def setUp(self):
        utils.set_up(self)

    def test_budget_creation_with_valid_data(self):
        budget = Budget.objects.create(
            property_cost=Decimal("100000.00"),
            property_cost_monthly=Decimal("8333.33"),
            salary=Decimal("5000.00"),
            period_start=timezone.now(),
            period_end=timezone.now() + timezone.timedelta(days=30)
        )
        self.assertIsNotNone(budget)

    def test_budget_string_representation(self):
        budget = Budget.objects.create(
            property_cost=Decimal("100000.00"),
            property_cost_monthly=Decimal("8333.33"),
            salary=Decimal("5000.00"),
            period_start=timezone.now(),
            period_end=timezone.now() + timezone.timedelta(days=30)
        )
        self.assertEqual(str(budget), f"{budget.period_start}-{budget.period_end}")

    def test_budget_with_negative_property_cost(self):
        with self.assertRaises(ValidationError):
            b = Budget.objects.create(
                property_cost=Decimal('-100000.00'),
                property_cost_monthly=Decimal("8333.33"),
                salary=Decimal("5000.00"),
                period_start=timezone.now(),
                period_end=timezone.now() + timezone.timedelta(days=30)
            )
            print(f" {b} ")

    def test_budget_with_negative_salary(self):
        with self.assertRaises(ValidationError):
            Budget.objects.create(
                property_cost=Decimal("100000.00"),
                property_cost_monthly=Decimal("8333.33"),
                salary=Decimal("-5000.00"),
                period_start=timezone.now(),
                period_end=timezone.now() + timezone.timedelta(days=30)
            )

    def test_budget_with_end_date_before_start_date(self):
        with self.assertRaises(ValidationError):
            Budget.objects.create(
                property_cost=Decimal("100000.00"),
                property_cost_monthly=Decimal("8333.33"),
                salary=Decimal("5000.00"),
                period_start=timezone.now(),
                period_end=timezone.now() - timezone.timedelta(days=30)
            )
