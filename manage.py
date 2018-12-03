#!/usr/bin/env python3
import os
import sys


# TODO: How to check if going to run tests?
if sys.argv[1] == "test":
    os.environ["NERU_ENV"] = "test"
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
else:
    os.environ.setdefault("NERU_ENV", "local")
    os.environ["DJANGO_SETTINGS_MODULE"] = f"proj.settings_{os.environ['NERU_ENV']}"

from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
