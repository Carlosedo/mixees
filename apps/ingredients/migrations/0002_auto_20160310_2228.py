# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spirit',
            name='volume',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
