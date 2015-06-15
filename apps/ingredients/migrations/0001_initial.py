# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=5, decimal_places=2)),
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
            name='Spirit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('slug', models.CharField(unique=True, max_length=20)),
                ('volume', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'Spirit',
                'verbose_name_plural': 'Spirits',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='mixer',
            field=models.ForeignKey(blank=True, to='ingredients.Mixer', null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='spirit',
            field=models.ForeignKey(blank=True, to='ingredients.Spirit', null=True),
        ),
    ]
