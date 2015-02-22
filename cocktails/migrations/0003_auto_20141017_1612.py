# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_mixer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('measurement', models.SmallIntegerField(choices=[(1, b'ml'), (2, b'oz'), (3, b'cup'), (4, b'part'), (5, b'teaspoon')])),
                ('mixers', models.ForeignKey(to='cocktails.Mixer')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='cocktails.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='spirits',
            field=models.ForeignKey(to='cocktails.Spirit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mixer',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='spirit',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
