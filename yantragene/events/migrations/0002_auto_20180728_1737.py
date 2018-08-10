# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-28 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eimage',
            field=models.ImageField(blank=True, upload_to='images/events'),
        ),
        migrations.AlterField(
            model_name='coordinator',
            name='cimage',
            field=models.ImageField(blank=True, upload_to='images/coordinators'),
        ),
    ]