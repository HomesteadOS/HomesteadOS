from django.test import TestCase

import home
from home.models.event import Event
from home.models.homestead import Homestead
from home.models.location import Location
from django.utils import timezone


class EventModelTest(TestCase):
    def setUp(self):
        home.tests.utils.set_up(self)

    def event_creation_with_different_start_date(self):
        different_start_date_event = Event.objects.create(
            start_date=(timezone.now() + timezone.timedelta(days=1)).date(),
            end_date=(timezone.now() + timezone.timedelta(days=2)).date(),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
            location=self.location,
            homestead=self.homestead
        )
        self.assertEqual(different_start_date_event.start_date, (timezone.now() + timezone.timedelta(days=1)).date())

    def event_string_representation(self):
        expected_string = self.event.start_date.__str__() + ' ' + self.event.start_time.__str__() + ' ' + self.event.location.name + ' @ ' + self.event.homestead.name
        self.assertEqual(str(self.event), expected_string)

    def event_creation_without_location(self):
        with self.assertRaises(ValueError):
            Event.objects.create(
                start_date=timezone.now().date(),
                end_date=(timezone.now() + timezone.timedelta(days=1)).date(),
                start_time=timezone.now().time(),
                end_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
                location=None,
                homestead=self.homestead
            )

    def event_creation_with_end_date_before_start_date(self):
        with self.assertRaises(ValueError):
            Event.objects.create(
                start_date=timezone.now().date(),
                end_date=(timezone.now() - timezone.timedelta(days=1)).date(),
                start_time=timezone.now().time(),
                end_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
                location=self.location,
                homestead=self.homestead
            )

    def event_creation_with_end_time_before_start_time(self):
        with self.assertRaises(ValueError):
            Event.objects.create(
                start_date=timezone.now().date(),
                end_date=timezone.now().date(),
                start_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
                end_time=timezone.now().time(),
                location=self.location,
                homestead=self.homestead
            )
