# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171207_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='count',
        ),
    ]