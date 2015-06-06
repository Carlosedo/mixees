# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0009_auto_20150606_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('measurement', models.SmallIntegerField(choices=[(1, b'ml'), (2, b'oz'), (3, b'cup'), (4, b'part'), (5, b'teaspoon')])),
                ('cocktail', models.ForeignKey(to='cocktails.Cocktail')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.CreateModel(
            name='Mixer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('slug', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Mixer',
                'verbose_name_plural': 'Mixers',
            },
        ),
        migrations.CreateModel(
            name='MixerIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('measurement', models.SmallIntegerField(choices=[(1, b'ml'), (2, b'oz'), (3, b'cup'), (4, b'part'), (5, b'teaspoon')])),
                ('cocktail', models.ForeignKey(to='cocktails.Cocktail')),
                ('mixers', models.ForeignKey(to='ingredients.Mixer')),
            ],
            options={
                'verbose_name': 'Miver Ingredient',
                'verbose_name_plural': 'Mixer Ingredients',
            },
        ),
        migrations.CreateModel(
            name='Spirit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('slug', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Spirit',
                'verbose_name_plural': 'Spirits',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='spirits',
            field=models.ForeignKey(to='ingredients.Spirit'),
        ),
    ]
