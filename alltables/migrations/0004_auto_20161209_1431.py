# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 14:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0003_auto_20160930_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 9, 14, 31, 18, 550333, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 9, 15, 31, 18, 550369, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]
