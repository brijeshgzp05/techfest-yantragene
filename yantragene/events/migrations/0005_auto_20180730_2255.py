# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-30 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_department_dimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinator',
            name='cdeptname',
        ),
        migrations.RemoveField(
            model_name='events',
            name='eimage',
        ),
    ]
