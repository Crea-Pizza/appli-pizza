# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='categorie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Categorie'),
        ),
    ]
