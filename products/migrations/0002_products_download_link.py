# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='download_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
