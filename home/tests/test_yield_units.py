from django.core.exceptions import ValidationError
from django.test import TestCase

import home
from home.models.yield_units import YieldUnits


class YieldUnitsModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_yield_unit_creation_with_different_name(self):
        different_name_yield_unit = YieldUnits.objects.create(name='Different Test YieldUnit', abbreviation='DYU')
        self.assertEqual(different_name_yield_unit.name, 'Different Test YieldUnit')

    def test_yield_unit_string_representation(self):
        expected_string = self.yield_unit.name
        self.assertEqual(str(self.yield_unit), expected_string)

    def test_yield_unit_creation_with_no_name(self):
        with self.assertRaises(ValidationError):
            YieldUnits.objects.create(name=None, abbreviation='No Name Test Abbreviation')
