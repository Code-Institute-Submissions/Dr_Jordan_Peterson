# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='book_author',
        ),
    ]
