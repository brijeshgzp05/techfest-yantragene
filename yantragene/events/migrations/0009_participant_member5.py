# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-03 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_participant_events_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='member5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]