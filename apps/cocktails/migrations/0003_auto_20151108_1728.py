# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastes', '0001_initial'),
        ('cocktails', '0002_remove_cocktail_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='glass_type',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='mixing_instructions',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='skill_level',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='tastes',
            field=models.ManyToManyField(to='tastes.Taste'),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='description',
            field=models.TextField(default=b''),
        ),
    ]
