from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from home.models.project import Project
from home.tests.utils import utils
from home.models.crop import Crop
from home.models.yield_units import YieldUnits


class CropTestCase(TestCase):
    def test_crop_creation_with_valid_data(self):
        yield_unit = YieldUnits.objects.create(name="Test Unit")
        crop = Crop.objects.create(
            name="Test Crop",
            description="Test Description",
            plant_date=timezone.now() + timezone.timedelta(days=10),
            harvest_date=timezone.now() + timezone.timedelta(days=90),
            harvest_target_date=timezone.now() + timezone.timedelta(days=80),
            yield_goal=1000,
            yield_unit=yield_unit,
            yield_actual=900
        )
        assert crop is not None


    def test_crop_string_representation(self):
        yield_unit = YieldUnits.objects.create(name="Test Unit")
        crop = Crop.objects.create(
            name="Test Crop",
            description="Test Description",
            plant_date=timezone.now() + timezone.timedelta(days=10),
            harvest_date=timezone.now() + timezone.timedelta(days=90),
            harvest_target_date=timezone.now() + timezone.timedelta(days=80),
            yield_goal=1000,
            yield_unit=yield_unit,
            yield_actual=900
        )
        assert str(crop) == "Test Crop"


    def test_crop_with_harvest_date_before_plant_date(self):
        with self.assertRaises(ValidationError):
            yield_unit = YieldUnits.objects.create(name="Test Unit")
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now(),
                harvest_date=timezone.now() - timezone.timedelta(days=90),
                harvest_target_date=timezone.now() + timezone.timedelta(days=80),
                yield_goal=1000,
                yield_unit=yield_unit,
                yield_actual=900
            )


    def test_crop_with_harvest_target_date_before_plant_date(self):
        with self.assertRaises(ValidationError):
            yield_unit = YieldUnits.objects.create(name="Test Unit")
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now(),
                harvest_date=timezone.now() + timezone.timedelta(days=90),
                harvest_target_date=timezone.now() - timezone.timedelta(days=80),
                yield_goal=1000,
                yield_unit=yield_unit,
                yield_actual=900
            )
            
    
    def test_crop_with_plant_date_in_the_past(self):
        with self.assertRaises(ValidationError):
            yield_unit = YieldUnits.objects.create(name="Test Unit")
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now() - timezone.timedelta(days=90),
                harvest_date=timezone.now() + timezone.timedelta(days=90),
                harvest_target_date=timezone.now() + timezone.timedelta(days=80),
                yield_goal=1000,
                yield_unit=yield_unit,
                yield_actual=900
            )

    def test_crop_with_negative_yield_goal(self):
        with self.assertRaises(ValidationError):
            yield_unit = YieldUnits.objects.create(name="Test Unit")
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now(),
                harvest_date=timezone.now() + timezone.timedelta(days=90),
                harvest_target_date=timezone.now() + timezone.timedelta(days=80),
                yield_goal=-1000,
                yield_unit=yield_unit,
                yield_actual=900
            )


    def test_crop_with_negative_yield_actual(self):
        with self.assertRaises(ValidationError):
            yield_unit = YieldUnits.objects.create(name="Test Unit")
            Crop.objects.create(
                name="Test Crop",
                description="Test Description",
                plant_date=timezone.now(),
                harvest_date=timezone.now() + timezone.timedelta(days=90),
                harvest_target_date=timezone.now() + timezone.timedelta(days=80),
                yield_goal=1000,
                yield_unit=yield_unit,
                yield_actual=-900
            )
