# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20171127_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_country',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]