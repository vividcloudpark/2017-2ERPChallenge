# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20171127_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailer',
            name='id',
        ),
        migrations.AlterField(
            model_name='retailer',
            name='company_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]