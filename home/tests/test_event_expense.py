from django.test import TestCase

import home
from home.models.event_expense import EventExpense
from home.models.event import Event


class EventExpenseModelTest(TestCase):
    def setUp(self):
        home.tests.utils.set_up(self)

    def event_expense_creation(self):
        self.assertEqual(self.event_expense.expense, self.expense)
        self.assertEqual(self.event_expense.event, self.event)

    def event_expense_string_representation(self):
        expected_string = self.event.__str__() + ' ' + self.expense.__str__()
        self.assertEqual(str(self.event_expense), expected_string)
