from django.test import TestCase
from home.models.task_list_notification import TaskListNotification
from home.models.staff import Staff
from home.models.task_list import TaskList
from django.utils import timezone


class TaskListNotificationModelTest(TestCase):
    def setUp(self):
        self.staff = Staff.objects.create(first_name='John', last_name='Doe')
        self.task_list = TaskList.objects.create(name='Test TaskList')
        self.task_list_notification = TaskListNotification.objects.create(
            task_list=self.task_list,
            staff=self.staff,
            datetime=timezone.now(),
            read=False
        )

    def task_list_notification_creation_with_different_staff(self):
        different_staff = Staff.objects.create(first_name='Jane', last_name='Doe')
        different_staff_task_list_notification = TaskListNotification.objects.create(
            task_list=self.task_list,
            staff=different_staff,
            datetime=timezone.now(),
            read=False
        )
        self.assertEqual(different_staff_task_list_notification.staff, different_staff)

    def task_list_notification_string_representation(self):
        expected_string = self.task_list_notification.task_list.name + ' ' + self.task_list_notification.staff.first_name + ' ' + self.task_list_notification.datetime.__str__()
        self.assertEqual(str(self.task_list_notification), expected_string)

    def task_list_notification_creation_without_task_list(self):
        with self.assertRaises(ValueError):
            TaskListNotification.objects.create(
                task_list=None,
                staff=self.staff,
                datetime=timezone.now(),
                read=False
            )

    def task_list_notification_read_status_change(self):
        self.task_list_notification.read = True
        self.task_list_notification.save()
        self.assertEqual(self.task_list_notification.read, True)
