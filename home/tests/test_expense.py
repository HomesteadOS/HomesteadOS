from django.core.exceptions import ValidationError
from django.test import TestCase

import home
from home.models.expense import Expense
from decimal import Decimal
from django.utils import timezone


class ExpenseModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_expense_creation_with_valid_data(self):
        self.assertEqual(self.expense.amount, Decimal('100.00'))
        self.assertEqual(self.expense.debt, Decimal('50.00'))
        self.assertEqual(self.expense.spender, self.staff)
        self.assertEqual(self.expense.debtor, self.staff)
        self.assertEqual(self.expense.description, 'Test Description')
        self.assertEqual(self.expense.percent, 50)
        self.assertEqual(self.expense.classification, self.expense_classification)
        self.assertEqual(self.expense.classification_detail, 'Test Classification Detail')
        self.assertEqual(self.expense.paid_external, False)
        self.assertEqual(self.expense.paid_internal, False)
        self.assertEqual(self.expense.approved, True)
        self.assertEqual(self.expense.store, 'Test Store')
        self.assertEqual(self.expense.supplier, self.supplier)

    def test_expense_string_representation(self):
        expected_string = self.expense.spender.last_name + ', ' + self.expense.spender.first_name + ' spent on ' + self.expense.datetime.__str__() + ' ' \
                          + self.expense.debtor.last_name + ', ' + self.expense.debtor.first_name + ' owes ' + str(
            self.expense.debt)
        self.assertEqual(str(self.expense), expected_string)

    def test_expense_creation_with_negative_amount(self):
        with self.assertRaises(ValidationError):
            Expense.objects.create(
                amount=Decimal('-100.00'),
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

    def test_expense_creation_with_negative_debt(self):
        with self.assertRaises(ValidationError):
            Expense.objects.create(
                amount=Decimal('100.00'),
                debt=Decimal('-50.00'),
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
