# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20190729_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etx_model',
            name='item_image',
            field=models.FileField(blank=True, default='etx_folder/arduino.jpg', upload_to=b''),
        ),
    ]
