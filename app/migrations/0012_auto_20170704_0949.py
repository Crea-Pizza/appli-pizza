# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170704_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='adresse2',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
    ]
