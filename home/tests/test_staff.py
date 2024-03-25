from django.test import TestCase
from home.models.staff import Staff
from home.models.location import Location


class StaffModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Test Location', coordinates='POINT(1 1)')
        self.staff = Staff.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            primary_location=self.location
        )

    def staff_creation_with_different_name(self):
        different_name_staff = Staff.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane.doe@example.com',
            primary_location=self.location
        )
        self.assertEqual(different_name_staff.first_name, 'Jane')

    def staff_string_representation(self):
        expected_string = self.staff.first_name + ' ' + self.staff.last_name
        self.assertEqual(str(self.staff), expected_string)

    def staff_creation_without_location(self):
        with self.assertRaises(ValueError):
            Staff.objects.create(
                first_name='No Location',
                last_name='Staff',
                email='no.location.staff@example.com',
                primary_location=None
            )

    def staff_email_change(self):
        self.staff.email = 'changed.email@example.com'
        self.staff.save()
        self.assertEqual(self.staff.email, 'changed.email@example.com')
