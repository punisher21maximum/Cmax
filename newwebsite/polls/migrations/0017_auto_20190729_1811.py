# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_calc_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etx_model',
            name='item_image',
            field=models.FileField(blank=True, default='book/pdf/no_image.jpg', upload_to=b''),
        ),
    ]
