# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0005_auto_20141019_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='MixerIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('measurement', models.SmallIntegerField(choices=[(1, b'ml'), (2, b'oz'), (3, b'cup'), (4, b'part'), (5, b'teaspoon')])),
                ('cocktail', models.ForeignKey(to='cocktails.Cocktail')),
                ('mixers', models.ForeignKey(to='cocktails.Mixer')),
            ],
            options={
                'verbose_name': 'Miver Ingredient',
                'verbose_name_plural': 'Mixer Ingredients',
            },
            bases=(models.Model,),
        ),
    ]
