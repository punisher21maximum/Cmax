# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-01 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20190801_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_desc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_topic',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_unit',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
