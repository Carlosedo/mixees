# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0006_mixeringredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='spirit',
            name='slug',
            field=models.CharField(default=datetime.date(2014, 11, 2), unique=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='slug',
            field=models.SlugField(unique=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='title',
            field=models.CharField(unique=True, max_length=80),
        ),
    ]
