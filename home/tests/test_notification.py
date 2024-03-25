from django.test import TestCase
from home.models.notification import Notification
from home.models.staff import Staff
from django.utils import timezone
import datetime


class NotificationModelTest(TestCase):
    def setUp(self):
        self.staff_member = Staff.objects.create(first_name='John', last_name='Doe')
        self.notification = Notification.objects.create(
            message='Test Message',
            staff=self.staff_member,
            datetime=timezone.now(),
            scheduled=False,
            scheduled_datetime=timezone.now() + datetime.timedelta(days=1),
            read=False
        )

    def notification_creation(self):
        self.assertEqual(self.notification.message, 'Test Message')
        self.assertEqual(self.notification.staff, self.staff_member)
        self.assertEqual(self.notification.scheduled, False)
        self.assertEqual(self.notification.read, False)

    def notification_scheduling(self):
        self.notification.scheduled = True
        self.notification.save()
        self.assertEqual(self.notification.scheduled, True)

    def notification_read_status(self):
        self.notification.read = True
        self.notification.save()
        self.assertEqual(self.notification.read, True)

    def notification_string_representation(self):
        expected_string = self.notification.message + ' ' + self.staff_member.first_name + ' ' + self.notification.datetime.__str__()
        self.assertEqual(str(self.notification), expected_string)
