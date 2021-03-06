# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160207_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
                ('data', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('malware', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Malware')),
            ],
        ),
    ]
