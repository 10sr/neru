import os

from django.contrib.auth.models import User

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin user"

    def add_arguments(self, parser):
        return

    def handle(self, *args, **kargs):
        username = "user"
        password = os.environ["LOCAL_USER_PASSWORD"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist as e:
            user = User.objects.create_user(username)

        user.set_password(password)
        user.save()
        return
