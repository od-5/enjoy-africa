# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_setup_robots_txt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='common',
            name='meta_desc',
        ),
        migrations.RemoveField(
            model_name='common',
            name='meta_keys',
        ),
        migrations.RemoveField(
            model_name='common',
            name='meta_title',
        ),
    ]
