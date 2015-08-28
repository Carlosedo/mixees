# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_liked_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='liked_posts',
            new_name='liked_cocktails',
        ),
    ]
