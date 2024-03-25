from django.test import TestCase
from home.models.task import Task
from home.models.homestead import Homestead
from home.models.staff import Staff
from django.utils import timezone


class TaskModelTest(TestCase):
    def setUp(self):
        self.homestead = Homestead.objects.create(name='Test Homestead')
        self.staff = Staff.objects.create(first_name='John', last_name='Doe')
        self.task = Task.objects.create(
            name='Test Task',
            description='Test Description',
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(hours=1),
            homestead=self.homestead,
            staff_responsible=self.staff,
            completed=False,
            comment='Test Comment'
        )

    def task_creation_with_different_name(self):
        different_name_task = Task.objects.create(
            name='Different Test Task',
            description='Test Description',
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(hours=1),
            homestead=self.homestead,
            staff_responsible=self.staff,
            completed=False,
            comment='Test Comment'
        )
        self.assertEqual(different_name_task.name, 'Different Test Task')

    def task_string_representation(self):
        expected_string = self.task.name
        self.assertEqual(str(self.task), expected_string)

    def task_creation_without_homestead(self):
        with self.assertRaises(ValueError):
            Task.objects.create(
                name='No Homestead Test Task',
                description='Test Description',
                start_date=timezone.now(),
                end_date=timezone.now() + timezone.timedelta(hours=1),
                homestead=None,
                staff_responsible=self.staff,
                completed=False,
                comment='Test Comment'
            )

    def task_creation_with_end_date_before_start_date(self):
        with self.assertRaises(ValueError):
            Task.objects.create(
                name='End Date Before Start Date Test Task',
                description='Test Description',
                start_date=timezone.now(),
                end_date=timezone.now() - timezone.timedelta(hours=1),
                homestead=self.homestead,
                staff_responsible=self.staff,
                completed=False,
                comment='Test Comment'
            )

    def task_completion_status_change(self):
        self.task.completed = True
        self.task.save()
        self.assertEqual(self.task.completed, True)
