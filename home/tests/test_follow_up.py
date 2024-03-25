from django.test import TestCase
from home.models.follow_up import FollowUp
from home.models.homestead import Homestead
from home.models.staff import Staff
from home.models.task import Task
from django.utils import timezone
import datetime


class FollowUpModelTest(TestCase):
    def setUp(self):
        self.homestead = Homestead.objects.create(name='Test Homestead')
        self.staff = Staff.objects.create(first_name='John', last_name='Doe')
        self.task = Task.objects.create(name='Test Task', description='Test Description')
        self.follow_up = FollowUp.objects.create(
            homestead=self.homestead,
            name='Test FollowUp',
            description='Test Description',
            staff_responsible=self.staff,
            due_date=timezone.now() + datetime.timedelta(days=1),
            completed=False,
            comment='Test Comment'
        )
        self.follow_up.tasks.add(self.task)

    def follow_up_creation_with_different_name(self):
        different_name_follow_up = FollowUp.objects.create(
            homestead=self.homestead,
            name='Different Test FollowUp',
            description='Test Description',
            staff_responsible=self.staff,
            due_date=timezone.now() + datetime.timedelta(days=1),
            completed=False,
            comment='Test Comment'
        )
        different_name_follow_up.tasks.add(self.task)
        self.assertEqual(different_name_follow_up.name, 'Different Test FollowUp')

    def follow_up_completion_status_change(self):
        self.follow_up.completed = True
        self.follow_up.save()
        self.assertEqual(self.follow_up.completed, True)

    def follow_up_string_representation(self):
        expected_string = self.follow_up.name
        self.assertEqual(str(self.follow_up), expected_string)

    def follow_up_creation_without_homestead(self):
        with self.assertRaises(ValueError):
            no_homestead_follow_up = FollowUp.objects.create(
                homestead=None,
                name='No Homestead Test FollowUp',
                description='Test Description',
                staff_responsible=self.staff,
                due_date=timezone.now() + datetime.timedelta(days=1),
                completed=False,
                comment='Test Comment'
            )
            no_homestead_follow_up.tasks.add(self.task)
