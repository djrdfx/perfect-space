# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160613_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-date_publication',), 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='project',
            name='date_publication',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='Дата публикации'),
        ),
    ]
