from django.core.management.base import BaseCommand, CommandError

from app.models import TimeOfSleep


class Command(BaseCommand):
    help = "Count sleep record num"

    def add_arguments(self, parser):
        return

    def handle(self, *args, **kargs):
        print(args)
        print(kargs)
        print(TimeOfSleep.objects.count())
        return
