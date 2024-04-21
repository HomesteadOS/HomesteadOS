from django.core.exceptions import ValidationError
from django.test import TestCase

import home
from home.models.event import Event
from django.utils import timezone


class EventModelTest(TestCase):
    def setUp(self):
        home.tests.utils.utils.set_up(self)

    def test_event_creation_with_valid_data(self):
        self.assertEqual(self.event.start_date, timezone.now().date())
        self.assertEqual(self.event.end_date, (timezone.now() + timezone.timedelta(days=1)).date())
        self.assertEqual(self.event.location, self.location)
        self.assertEqual(self.event.homestead, self.homestead)
        self.assertEqual(self.event.staff_responsible, self.staff)

    def test_event_string_representation(self):
        expected_string = self.event.start_date.__str__() + ' ' + self.event.start_time.__str__() + ' ' + self.event.location.name + ' @ ' + self.event.homestead.name
        self.assertEqual(str(self.event), expected_string)

    def test_event_creation_with_end_date_before_start_date(self):
        with self.assertRaises(ValidationError):
            Event.objects.create(
                start_date=timezone.now().date(),
                end_date=(timezone.now() - timezone.timedelta(days=1)).date(),
                start_time=timezone.now().time(),
                end_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
                location=self.location,
                homestead=self.homestead,
                staff_responsible=self.staff
            )

    def test_event_creation_with_end_time_before_start_time(self):
        with self.assertRaises(ValidationError):
            Event.objects.create(
                start_date=timezone.now().date(),
                end_date=timezone.now().date(),
                start_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
                end_time=timezone.now().time(),
                location=self.location,
                homestead=self.homestead,
                staff_responsible=self.staff
            )
