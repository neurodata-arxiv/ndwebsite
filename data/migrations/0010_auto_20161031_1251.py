# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20161031_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataproject',
            name='background_image',
            field=models.CharField(default='/assets/img/tools/default_header.jpg', max_length=128),
        ),
    ]
