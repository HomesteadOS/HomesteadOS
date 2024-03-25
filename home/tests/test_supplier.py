from django.test import TestCase
from home.models.supplier import Supplier
from home.models.location import Location


class SupplierModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Test Location', coordinates='POINT(1 1)')
        self.supplier = Supplier.objects.create(
            name='Test Supplier',
            description='Test Description',
            location=self.location
        )

    def supplier_creation_with_different_name(self):
        different_name_supplier = Supplier.objects.create(
            name='Different Test Supplier',
            description='Test Description',
            location=self.location
        )
        self.assertEqual(different_name_supplier.name, 'Different Test Supplier')

    def supplier_string_representation(self):
        expected_string = self.supplier.name
        self.assertEqual(str(self.supplier), expected_string)

    def supplier_creation_without_location(self):
        with self.assertRaises(ValueError):
            Supplier.objects.create(
                name='No Location Test Supplier',
                description='Test Description',
                location=None
            )

    def supplier_description_change(self):
        self.supplier.description = 'Changed Description'
        self.supplier.save()
        self.assertEqual(self.supplier.description, 'Changed Description')
