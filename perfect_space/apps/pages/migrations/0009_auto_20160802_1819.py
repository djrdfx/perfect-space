# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20160802_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainimage',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]
