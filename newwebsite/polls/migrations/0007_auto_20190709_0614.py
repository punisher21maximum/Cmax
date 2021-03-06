# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-09 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190425_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_model',
            name='star',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='novel_model',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='novel_model',
            name='pages',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
