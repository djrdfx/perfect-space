# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(choices=[('index', 'Главная'), ('about', 'О Нас')], max_length=50, verbose_name='Шаблон'),
        ),
    ]