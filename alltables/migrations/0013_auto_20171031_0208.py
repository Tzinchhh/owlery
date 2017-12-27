# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-31 02:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0012_auto_20171031_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 2, 8, 21, 982999, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 3, 8, 21, 983029, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]
