# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-30 23:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0007_auto_20171030_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 23, 23, 9, 724836, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 0, 23, 9, 724865, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]