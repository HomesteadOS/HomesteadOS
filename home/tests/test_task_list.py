from django.test import TestCase
from home.models.task_list import TaskList
from home.models.homestead import Homestead
from home.models.staff import Staff
from home.models.task import Task
from django.utils import timezone


class TaskListModelTest(TestCase):
    def setUp(self):
        self.homestead = Homestead.objects.create(name='Test Homestead')
        self.staff = Staff.objects.create(first_name='John', last_name='Doe')
        self.task = Task.objects.create(name='Test Task', description='Test Description')
        self.task_list = TaskList.objects.create(
            homestead=self.homestead,
            name='Test TaskList',
            staff_responsible=self.staff,
            description='Test Description',
            due_date=timezone.now(),
            start_date=timezone.now()
        )
        self.task_list.tasks.add(self.task)

    def task_list_creation_with_different_name(self):
        different_name_task_list = TaskList.objects.create(
            homestead=self.homestead,
            name='Different Test TaskList',
            staff_responsible=self.staff,
            description='Test Description',
            due_date=timezone.now(),
            start_date=timezone.now()
        )
        self.assertEqual(different_name_task_list.name, 'Different Test TaskList')

    def task_list_string_representation(self):
        expected_string = self.task_list.name
        self.assertEqual(str(self.task_list), expected_string)

    def task_list_creation_without_homestead(self):
        with self.assertRaises(ValueError):
            TaskList.objects.create(
                homestead=None,
                name='No Homestead Test TaskList',
                staff_responsible=self.staff,
                description='Test Description',
                due_date=timezone.now(),
                start_date=timezone.now()
            )

    def task_list_creation_with_due_date_before_start_date(self):
        with self.assertRaises(ValueError):
            TaskList.objects.create(
                homestead=self.homestead,
                name='Due Date Before Start Date Test TaskList',
                staff_responsible=self.staff,
                description='Test Description',
                due_date=timezone.now(),
                start_date=timezone.now() + timezone.timedelta(days=1)
            )

    def task_list_add_task(self):
        new_task = Task.objects.create(name='New Test Task', description='Test Description')
        self.task_list.tasks.add(new_task)
        self.assertIn(new_task, self.task_list.tasks.all())
