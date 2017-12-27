# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-27 12:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0020_auto_20171117_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='field2',
            new_name='username',
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=1000),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 12, 24, 51, 813181, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 13, 24, 51, 813212, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]