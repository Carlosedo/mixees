# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0004_remove_cocktail_tastes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='total_parts',
            field=models.IntegerField(default=0),
        ),
    ]
