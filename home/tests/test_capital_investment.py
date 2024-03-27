from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from home.models.capital_investment import CapitalInvestment
from home.models.project import Project
from home.tests.utils import utils


class CapitalInvestmentTestCase(TestCase):
    def setUp(self):
        utils.set_up(self)

    def test_capital_investment_creation_with_valid_data(self):
        capital_investment = CapitalInvestment.objects.create(project=self.project, description="Test Description"
                                                              , investment_amount=10000.00
                                                              , investment_date=utils.timezone.now())
        self.assertTrue(capital_investment is not None)

    def test_capital_investment_string_representation(self):
        capital_investment = CapitalInvestment.objects.create(project=self.project, description="Test Description"
                                                              , investment_amount=10000.00
                                                              , investment_date=utils.timezone.now())
        self.assertEqual(str(capital_investment), "Test Project")

    def test_capital_investment_creation_without_project(self):
        with self.assertRaises(ValidationError):
            CapitalInvestment.objects.create(description="Test Description"
                                             , investment_amount=10000.00
                                             , investment_date=utils.timezone.now())

    def test_capital_investment_creation_without_description(self):
        with self.assertRaises(ValidationError):
            capital_investment = CapitalInvestment.objects.create(project=self.project,
                                                                investment_amount=10000.00,
                                                                investment_date=utils.timezone.now())

