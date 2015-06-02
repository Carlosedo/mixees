# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0007_auto_20141102_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixer',
            name='slug',
            field=models.CharField(default=datetime.date(2014, 11, 2), unique=True, max_length=20),
            preserve_default=False,
        ),
    ]
