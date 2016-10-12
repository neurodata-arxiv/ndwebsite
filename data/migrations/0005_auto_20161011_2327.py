# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20161011_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproject',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataproject',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
