# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-02 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='events_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
