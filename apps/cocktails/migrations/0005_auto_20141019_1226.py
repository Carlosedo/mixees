# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0004_remove_ingredient_mixers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Cocktail',
        ),
        migrations.AlterModelOptions(
            name='cocktail',
            options={'verbose_name': 'Cocktail', 'verbose_name_plural': 'Cocktails'},
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe',
            new_name='cocktail',
        ),
    ]
