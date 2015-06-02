# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_auto_20141017_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='mixers',
        ),
    ]
