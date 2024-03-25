from django.test import TestCase
from home.models.task_list_log import TaskListLog
from home.models.staff import Staff
from home.models.task_list import TaskList
from django.utils import timezone


class TaskListLogModelTest(TestCase):
    def setUp(self):
        self.staff = Staff.objects.create(first_name='John', last_name='Doe')
        self.task_list = TaskList.objects.create(name='Test TaskList')
        self.task_list_log = TaskListLog.objects.create(
            task_list=self.task_list,
            staff=self.staff,
            datetime=timezone.now(),
            comment='Test Comment'
        )

    def task_list_log_creation_with_different_staff(self):
        different_staff = Staff.objects.create(first_name='Jane', last_name='Doe')
        different_staff_task_list_log = TaskListLog.objects.create(
            task_list=self.task_list,
            staff=different_staff,
            datetime=timezone.now(),
            comment='Test Comment'
        )
        self.assertEqual(different_staff_task_list_log.staff, different_staff)

    def task_list_log_string_representation(self):
        expected_string = self.task_list_log.task_list.name + ' ' + self.task_list_log.staff.first_name + ' ' + self.task_list_log.datetime.__str__()
        self.assertEqual(str(self.task_list_log), expected_string)

    def task_list_log_creation_without_task_list(self):
        with self.assertRaises(ValueError):
            TaskListLog.objects.create(
                task_list=None,
                staff=self.staff,
                datetime=timezone.now(),
                comment='Test Comment'
            )

    def task_list_log_comment_change(self):
        self.task_list_log.comment = 'Changed Comment'
        self.task_list_log.save()
        self.assertEqual(self.task_list_log.comment, 'Changed Comment')
