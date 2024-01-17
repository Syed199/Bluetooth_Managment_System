# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20170411_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerstudent',
            name='baddr',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
