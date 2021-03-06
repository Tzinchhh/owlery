# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-13 23:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0013_auto_20171031_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letters',
            old_name='to_adr',
            new_name='send_to',
        ),
        migrations.RemoveField(
            model_name='letters',
            name='arrival',
        ),
        migrations.RemoveField(
            model_name='letters',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='letters',
            name='reading_time',
        ),
        migrations.RemoveField(
            model_name='letters',
            name='title',
        ),
        migrations.AlterField(
            model_name='letters',
            name='from_adr',
            field=models.CharField(blank=True, max_length=200, verbose_name='От кого'),
        ),
        migrations.AlterField(
            model_name='letters',
            name='owl_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 23, 56, 40, 587799, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 0, 56, 40, 587831, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]
