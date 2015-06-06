# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0008_mixer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='cocktail',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='spirits',
        ),
        migrations.RemoveField(
            model_name='mixeringredient',
            name='cocktail',
        ),
        migrations.RemoveField(
            model_name='mixeringredient',
            name='mixers',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Mixer',
        ),
        migrations.DeleteModel(
            name='MixerIngredient',
        ),
        migrations.DeleteModel(
            name='Spirit',
        ),
    ]
