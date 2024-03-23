import pytest
from django.utils import timezone
from home.models.crop import Crop
from home.models.yield_units import YieldUnits


def crop_creation_with_valid_data():
    yield_unit = YieldUnits.objects.create(name="Test Unit")
    crop = Crop.objects.create(
        name="Test Crop",
        description="Test Description",
        plant_date=timezone.now(),
        harvest_date=timezone.now() + timezone.timedelta(days=90),
        harvest_target_date=timezone.now() + timezone.timedelta(days=80),
        yield_goal=1000,
        yield_unit=yield_unit,
        yield_actual=900
    )
    assert crop is not None


def crop_string_representation():
    yield_unit = YieldUnits.objects.create(name="Test Unit")
    crop = Crop.objects.create(
        name="Test Crop",
        description="Test Description",
        plant_date=timezone.now(),
        harvest_date=timezone.now() + timezone.timedelta(days=90),
        harvest_target_date=timezone.now() + timezone.timedelta(days=80),
        yield_goal=1000,
        yield_unit=yield_unit,
        yield_actual=900
    )
    assert str(crop) == "Test Crop"


def crop_with_harvest_date_before_plant_date():
    with pytest.raises(ValueError):
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


def crop_with_negative_yield_goal():
    with pytest.raises(ValueError):
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


def crop_with_negative_yield_actual():
    with pytest.raises(ValueError):
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
