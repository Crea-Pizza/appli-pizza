# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170703_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='nom',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='personne',
            name='prenom',
            field=models.CharField(blank=True, default=None, max_length=15),
        ),
    ]