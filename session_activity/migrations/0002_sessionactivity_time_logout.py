# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionactivity',
            name='time_logout',
            field=models.DateTimeField(null=True),
        ),
    ]
