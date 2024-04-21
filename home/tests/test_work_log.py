from django.core.exceptions import ValidationError
from django.test import TestCase

import home
from home.models.work_log import WorkLog
from home.models.staff import Staff
from home.models.task import Task
from django.utils import timezone


class WorkLogModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_work_log_creation_with_valid_data(self):
        self.assertEqual(self.work_log.task, self.task)
        self.assertEqual(self.work_log.staff, self.staff)
        self.assertEqual(self.work_log.comment, 'Test Comment')

    def test_work_log_string_representation(self):
        expected_string = self.work_log.task.name + ' ' + self.work_log.staff.first_name + ' ' + self.work_log.start_time.__str__() + ' ' + self.work_log.end_time.__str__()
        self.assertEqual(str(self.work_log), expected_string)

    def test_work_log_creation_with_end_time_before_start_time(self):
        with self.assertRaises(ValidationError):
            WorkLog.objects.create(
                task=self.task,
                staff=self.staff,
                start_time=timezone.now() + timezone.timedelta(hours=1),
                end_time=timezone.now(),
                comment='Test Comment'
            )
