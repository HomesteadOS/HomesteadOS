from django.test import TestCase
from home.models.field import Field
from home.models.location import Location
from home.models.crop import Crop


class FieldModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Test Location')
        self.crop = Crop.objects.create(name='Test Crop')
        self.field = Field.objects.create(location=self.location, crop=self.crop)

    def field_creation_with_different_location(self):
        different_location = Location.objects.create(name='Different Test Location')
        different_location_field = Field.objects.create(location=different_location, crop=self.crop)
        self.assertEqual(different_location_field.location, different_location)

    def field_creation_with_no_crop(self):
        no_crop_field = Field.objects.create(location=self.location, crop=None)
        self.assertEqual(no_crop_field.crop, None)

    def field_string_representation(self):
        expected_string = self.field.name
        self.assertEqual(str(self.field), expected_string)

    def field_creation_without_location(self):
        with self.assertRaises(ValueError):
            Field.objects.create(location=None, crop=self.crop)
