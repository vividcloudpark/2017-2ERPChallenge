# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20171127_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=50),
        ),
    ]
