# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160207_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='type',
            field=models.CharField(max_length=120),
        ),
    ]
