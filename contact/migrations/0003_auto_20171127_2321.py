# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20171127_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_name',
            field=models.CharField(max_length=20),
        ),
    ]