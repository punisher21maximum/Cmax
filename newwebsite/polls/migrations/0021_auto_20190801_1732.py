# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-01 17:32
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_remove_enotes_model_enotes_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_author',
            field=models.CharField(blank=True, default=django.contrib.auth.models.User, max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_desc',
            field=models.CharField(blank=True, default='say something...', max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_topic',
            field=models.CharField(blank=True, default='topic', max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_unit',
            field=models.CharField(blank=True, default='enter integer', max_length=100),
        ),
    ]
