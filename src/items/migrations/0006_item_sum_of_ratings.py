# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20171016_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sum_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
