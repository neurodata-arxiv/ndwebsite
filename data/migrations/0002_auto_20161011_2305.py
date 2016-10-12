# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExploreTile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('author', models.CharField(blank=True, max_length=255)),
                ('modality', models.CharField(blank=True, max_length=255)),
                ('species', models.CharField(blank=True, max_length=255)),
                ('cuboids', models.CharField(blank=True, max_length=255)),
                ('cuboid_size', models.CharField(blank=True, max_length=255)),
                ('voxels', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='/upload/tile/explore/')),
                ('subcategory', models.CharField(choices=[('Images', 'Images'), ('Time', 'Time'), ('Matrices', 'Matrices'), ('Shapes', 'Shapes'), ('Graphs', 'Graphs')], max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='DataLink',
        ),
    ]
