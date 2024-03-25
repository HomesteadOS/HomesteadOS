from django.test import TestCase
from home.models.homestead import Homestead


class HomesteadModelTest(TestCase):
    def setUp(self):
        self.homestead = Homestead.objects.create(name='Test Homestead', description='Test Description')

    def homestead_creation_with_different_name(self):
        different_name_homestead = Homestead.objects.create(name='Different Test Homestead',
                                                            description='Test Description')
        self.assertEqual(different_name_homestead.name, 'Different Test Homestead')

    def homestead_string_representation(self):
        expected_string = self.homestead.name
        self.assertEqual(str(self.homestead), expected_string)

    def homestead_creation_with_no_name(self):
        with self.assertRaises(ValueError):
            Homestead.objects.create(name=None, description='No Name Test Description')
