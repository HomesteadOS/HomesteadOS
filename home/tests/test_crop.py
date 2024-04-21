from django.core.exceptions import ValidationError
from django.test import TestCase

import home.tests.utils.utils
from home.models.crop import Crop
from home.models.yield_units import YieldUnits
from django.utils import timezone
from decimal import Decimal


class CropModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_crop_creation_with_valid_data(self):
        self.assertEqual(self.crop.name, "Test Crop")
        self.assertEqual(self.crop.description, "Test Description")
        self.assertEqual(self.crop.yield_goal, Decimal('1000.00'))
        self.assertEqual(self.crop.yield_unit, self.yield_unit)
        self.assertEqual(self.crop.yield_actual, Decimal('900.00'))

    def test_crop_string_representation(self):
        self.assertEqual(str(self.crop), "Test Crop")

    def test_crop_creation_with_negative_yield_goal(self):
        with self.assertRaises(ValidationError):
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now(),
                harvest_date=timezone.now() + timezone.timedelta(days=90),
                harvest_target_date=timezone.now() + timezone.timedelta(days=80),
                yield_goal=Decimal('-1000.00'),
                yield_unit=self.yield_unit,
                yield_actual=Decimal('900.00')
            )

    def test_crop_creation_with_negative_yield_actual(self):
        with self.assertRaises(ValidationError):
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now(),
                harvest_date=timezone.now() + timezone.timedelta(days=90),
                harvest_target_date=timezone.now() + timezone.timedelta(days=80),
                yield_goal=Decimal('1000.00'),
                yield_unit=self.yield_unit,
                yield_actual=Decimal('-900.00')
            )
