from django.test import TestCase
from home.models.location import Location
from home.models.homestead import Homestead

class LocationModelTest(TestCase):
    def setUp(self):
        self.homestead = Homestead.objects.create(name='Test Homestead')
        self.location = Location.objects.create(
            homestead=self.homestead,
            name='Test Location',
            description='Test Description',
            primary_location=False
        )

    def location_creation_with_different_name(self):
        different_name_location = Location.objects.create(
            homestead=self.homestead,
            name='Different Test Location',
            description='Test Description',
            primary_location=False
        )
        self.assertEqual(different_name_location.name, 'Different Test Location')

    def location_primary_status_change(self):
        self.location.primary_location = True
        self.location.save()
        self.assertEqual(self.location.primary_location, True)

    def location_string_representation(self):
        expected_string = self.location.name
        self.assertEqual(str(self.location), expected_string)

    def location_creation_without_homestead(self):
        with self.assertRaises(ValueError):
            Location.objects.create(
                homestead=None,
                name='No Homestead Test Location',
                description='Test Description',
                primary_location=False
            )