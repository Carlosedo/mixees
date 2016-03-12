# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_auto_20160310_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(default=b'Some', max_length=30),
        ),
    ]
