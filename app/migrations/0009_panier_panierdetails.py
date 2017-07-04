# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_pizza_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, help_text='Date quand le panier est créé')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PanierDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveSmallIntegerField(help_text='Quantité')),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panier_detail', to='app.Panier')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pizza')),
            ],
        ),
    ]
