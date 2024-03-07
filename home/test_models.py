from datetime import datetime, timedelta

import HomesteadModelTestCase
from home.models import Homestead, Location, Staff, RoleClasses, \
    Role, YieldUnits, Crop, Field, Supplier, Expense, ExpenseClassification, \
    Project, CapitalInvestment, Budget


class TestProject(HomesteadModelTestCase):
    sup = None

    def __init__(self):
        super.__init__(self)
        self.sup = super()

    def test_project_model(self):
        actual = Project.objects.get(name=self.sup.project.name)
        expected = self.sup.project
        self.assertIsNotNone(actual)
        self.assertEqual(actual.description, expected.description)
        self.assertEqual(actual.homestead, expected.homestead)
        self.assertEqual(actual.due_date, expected.due_date)
        self.assertEqual(actual.staff_responsible, expected.staff_responsible)
        self.assertEqual(actual.start_date, expected.start_date)


class TestHomestead(HomesteadModelTestCase):
    sup = None

    def test_homestead_model(self):
        actual = Homestead.objects.get(name=self.sup.mermaid.name)
        expected = self.sup.mermaid
        self.assertIsNotNone(actual)
        self.assertEqual(actual.description, expected.description)


class TestLocation(HomesteadModelTestCase):
    sup = None

    def test_location_models(self) -> None:
        fuller = Location.objects.get(name="Fuller Rd")
        corpse_hall = Location.objects.get(name="Corpse Hall")
        hel = Location.objects.get(name="Hel")
        self.assertEqual(fuller.name, self.sup.fuller.name)
        self.assertEqual(corpse_hall.name, self.sup.corpse_hall.name)
        self.assertEqual(hel.name, self.sup.hel.name)
        self.assertEqual(fuller.primary_location, self.sup.fuller.primary_location)
        self.assertEqual(corpse_hall.primary_location, self.sup.corpse_hall.primary_location)
        self.assertEqual(hel.primary_location, self.sup.hel.primary_location)
        self.assertIsNotNone(fuller.description)
        self.assertIsNotNone(corpse_hall.description)
        self.assertIsNotNone(hel.description)