# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-31 01:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alltables', '0008_auto_20171030_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000, verbose_name='Логин')),
                ('password', models.CharField(max_length=1000, verbose_name='Пароль')),
            ],
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 1, 12, 34, 49862, tzinfo=utc), verbose_name='Время вылета совы'),
        ),
        migrations.AlterField(
            model_name='owls',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 31, 2, 12, 34, 49893, tzinfo=utc), verbose_name='Время прилета совы'),
        ),
    ]