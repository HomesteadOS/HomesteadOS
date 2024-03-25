from django.test import TestCase
from home.models.yield_units import YieldUnits


class YieldUnitsModelTest(TestCase):
    def setUp(self):
        self.yield_unit = YieldUnits.objects.create(name='Test YieldUnit', abbreviation='TYU')

    def yield_unit_creation_with_different_name(self):
        different_name_yield_unit = YieldUnits.objects.create(name='Different Test YieldUnit', abbreviation='DTYU')
        self.assertEqual(different_name_yield_unit.name, 'Different Test YieldUnit')

    def yield_unit_string_representation(self):
        expected_string = self.yield_unit.name
        self.assertEqual(str(self.yield_unit), expected_string)

    def yield_unit_creation_with_no_name(self):
        with self.assertRaises(ValueError):
            YieldUnits.objects.create(name=None, abbreviation='No Name Test Abbreviation')

    def yield_unit_creation_with_same_name(self):
        with self.assertRaises(ValueError):
            YieldUnits.objects.create(name='Test YieldUnit', abbreviation='SYU')
