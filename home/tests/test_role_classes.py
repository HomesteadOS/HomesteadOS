from django.test import TestCase
from home.models.role_classes import RoleClasses


class RoleClassesModelTest(TestCase):
    def setUp(self):
        self.role_class = RoleClasses.objects.create(
            name='Test RoleClass',
            description='Test Description',
            enabled=True
        )

    def role_class_creation_with_different_name(self):
        different_name_role_class = RoleClasses.objects.create(
            name='Different Test RoleClass',
            description='Test Description',
            enabled=True
        )
        self.assertEqual(different_name_role_class.name, 'Different Test RoleClass')

    def role_class_string_representation(self):
        expected_string = self.role_class.name
        self.assertEqual(str(self.role_class), expected_string)

    def role_class_creation_with_same_name(self):
        with self.assertRaises(ValueError):
            RoleClasses.objects.create(
                name='Test RoleClass',
                description='Test Description',
                enabled=True
            )

    def role_class_enabled_status_change(self):
        self.role_class.enabled = False
        self.role_class.save()
        self.assertEqual(self.role_class.enabled, False)
