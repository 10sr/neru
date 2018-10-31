from django.utils import timezone
from django.test import TestCase

from app import models


class TimeOfSleepTests(TestCase):
    def test_add_record(self):
        now = timezone.now()
        tos = models.TimeOfSleep(
            time_of_sleep=now,
            datetime=now,
            id_str="12345",
            note="NOTE"
        )
        print(str(tos))
        return
