# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160606_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(choices=[('index', 'Главная'), ('about', 'О Нас'), ('projects', 'Проекты')], max_length=50, verbose_name='Шаблон'),
        ),
    ]