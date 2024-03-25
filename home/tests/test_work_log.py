from django.test import TestCase
from home.models.work_log import WorkLog
from home.models.staff import Staff
from home.models.task import Task
from django.utils import timezone
import datetime


class WorkLogModelTest(TestCase):
    def setUp(self):
        self.staff = Staff.objects.create(first_name='John', last_name='Doe')
        self.task = Task.objects.create(name='Test Task', description='Test Description')
        self.work_log = WorkLog.objects.create(
            task=self.task,
            staff=self.staff,
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(hours=1),
            comment='Test Comment'
        )

    def work_log_creation_with_different_staff(self):
        different_staff = Staff.objects.create(first_name='Jane', last_name='Doe')
        different_staff_work_log = WorkLog.objects.create(
            task=self.task,
            staff=different_staff,
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(hours=1),
            comment='Test Comment'
        )
        self.assertEqual(different_staff_work_log.staff, different_staff)

    def work_log_string_representation(self):
        expected_string = self.work_log.task.name + ' ' + self.work_log.staff.first_name + ' ' + self.work_log.start_time.__str__() + ' ' + self.work_log.end_time.__str__()
        self.assertEqual(str(self.work_log), expected_string)

    def work_log_creation_without_task(self):
        with self.assertRaises(ValueError):
            WorkLog.objects.create(
                task=None,
                staff=self.staff,
                start_time=timezone.now(),
                end_time=timezone.now() + datetime.timedelta(hours=1),
                comment='Test Comment'
            )

    def work_log_creation_with_end_time_before_start_time(self):
        with self.assertRaises(ValueError):
            WorkLog.objects.create(
                task=self.task,
                staff=self.staff,
                start_time=timezone.now(),
                end_time=timezone.now() - datetime.timedelta(hours=1),
                comment='Test Comment'
            )
