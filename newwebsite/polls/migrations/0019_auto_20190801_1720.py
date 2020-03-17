# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-01 17:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20190731_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enotes_model',
            name='enotes_author_name',
        ),
        migrations.AddField(
            model_name='enotes_model',
            name='enotes_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='enotes_model',
            name='enotes_desc',
            field=models.CharField(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AddField(
            model_name='enotes_model',
            name='enotes_topic',
            field=models.CharField(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AddField(
            model_name='enotes_model',
            name='enotes_unit',
            field=models.CharField(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_author',
            field=models.CharField(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AlterField(
            model_name='enotes_model',
            name='enotes_drive_url',
            field=models.URLField(default='http://localhost:8000/polls/', max_length=100, null=True),
        ),
    ]
