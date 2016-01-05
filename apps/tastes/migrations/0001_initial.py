# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=80)),
                ('slug', models.SlugField(unique=True, max_length=80)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Taste',
                'verbose_name_plural': 'Tastes',
            },
        ),
    ]
