# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-29 04:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181026_1336'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TwitterUsername',
            new_name='TwitterUser',
        ),
    ]