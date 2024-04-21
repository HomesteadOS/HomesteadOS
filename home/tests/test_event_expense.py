from django.test import TestCase

import home


class EventExpenseModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_event_expense_creation(self):
        self.assertEqual(self.event_expense.expense, self.expense)
        self.assertEqual(self.event_expense.event, self.event)

    def test_event_expense_string_representation(self):
        expected_string = self.event.__str__() + ' ' + self.expense.__str__()
        self.assertEqual(str(self.event_expense), expected_string)
