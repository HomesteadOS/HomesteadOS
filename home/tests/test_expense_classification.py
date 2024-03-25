from django.test import TestCase
from home.models.expense_classification import ExpenseClassification


class ExpenseClassificationModelTest(TestCase):
    def setUp(self):
        self.expense_classification = ExpenseClassification.objects.create(name='Test ExpenseClassification',
                                                                           description='Test Description')

    def expense_classification_creation_with_different_name(self):
        different_name_expense_classification = ExpenseClassification.objects.create(
            name='Different Test ExpenseClassification', description='Test Description')
        self.assertEqual(different_name_expense_classification.name, 'Different Test ExpenseClassification')

    def expense_classification_string_representation(self):
        expected_string = self.expense_classification.name
        self.assertEqual(str(self.expense_classification), expected_string)

    def expense_classification_creation_with_no_name(self):
        with self.assertRaises(ValueError):
            ExpenseClassification.objects.create(name=None, description='No Name Test Description')
