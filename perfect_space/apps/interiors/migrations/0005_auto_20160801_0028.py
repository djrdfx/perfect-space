# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-31 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0004_auto_20160725_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interior',
            name='bedrooms',
            field=models.CharField(blank=True, max_length=100, verbose_name='Спален'),
        ),
    ]