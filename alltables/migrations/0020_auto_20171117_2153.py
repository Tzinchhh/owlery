# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-17 21:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0019_auto_20171117_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letters',
            old_name='send_to2',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 21, 53, 36, 694328, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 22, 53, 36, 694357, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]
