from django.test import TestCase
from home.models.expense import Expense
from decimal import Decimal
from django.utils import timezone

from home.tests.utils import utils


class ExpenseModelTest(TestCase):
    def setUp(self):
        utils.set_up(self)

    def expense_creation_with_different_amount(self):
        different_amount_expense = Expense.objects.create(
            amount=Decimal('200.00'),
            debt=Decimal('100.00'),
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
        self.assertEqual(different_amount_expense.amount, Decimal('200.00'))

    def expense_string_representation(self):
        expected_string = self.expense.spender.last_name + ', ' + self.expense.spender.first_name + ' spent on ' + self.expense.datetime.__str__() + ' ' + self.expense.debtor.last_name + ', ' + self.expense.debtor.first_name + ' owes ' + str(
            self.expense.debt)
        self.assertEqual(str(self.expense), expected_string)

    def expense_creation_with_debt_greater_than_amount(self):
        with self.assertRaises(ValueError):
            Expense.objects.create(
                amount=Decimal('100.00'),
                debt=Decimal('200.00'),
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

    def expense_paid_status_change(self):
        self.expense.paid_external = True
        self.expense.save()
        self.assertEqual(self.expense.paid_external, True)
