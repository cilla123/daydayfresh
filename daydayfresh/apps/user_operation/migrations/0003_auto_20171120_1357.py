# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 13:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20171120_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 57, 6, 558333), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 57, 6, 556443), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 57, 6, 557776), verbose_name='添加时间'),
        ),
    ]
