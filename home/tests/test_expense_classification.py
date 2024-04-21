from django.core.exceptions import ValidationError
from django.test import TestCase

import home
from home.models.expense_classification import ExpenseClassification


class ExpenseClassificationModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_expense_classification_creation_with_different_name(self):
        different_name_expense_classification = ExpenseClassification.objects.create(
            name='Different Test ExpenseClassification', description='Test Description')
        self.assertEqual(different_name_expense_classification.name, 'Different Test ExpenseClassification')

    def test_expense_classification_string_representation(self):
        expected_string = self.expense_classification.name
        self.assertEqual(str(self.expense_classification), expected_string)

    def test_expense_classification_creation_with_no_name(self):
        with self.assertRaises(ValidationError):
            ExpenseClassification.objects.create(name=None, description='No Name Test Description')
