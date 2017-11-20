# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目类别', verbose_name='类目类别')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 818081), help_text='添加时间', verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父类目级别', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='goods.GoodsCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.RemoveField(
            model_name='goodscaegory',
            name='parent_category',
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 820814), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 819507), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_front_image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 818653), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 13, 26, 26, 820229), verbose_name='添加时间'),
        ),
        migrations.DeleteModel(
            name='GoodsCaegory',
        ),
    ]