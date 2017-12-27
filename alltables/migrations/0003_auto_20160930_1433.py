# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 14:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0002_auto_20160930_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 14, 33, 30, 589909, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 15, 33, 30, 589944, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]