# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20171120_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 823060), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 822492), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 821751), verbose_name='添加时间'),
        ),
    ]
