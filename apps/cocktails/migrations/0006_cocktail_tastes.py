# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastes', '0001_initial'),
        ('cocktails', '0005_cocktail_total_parts'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='tastes',
            field=models.ManyToManyField(to='tastes.Taste'),
        ),
    ]
