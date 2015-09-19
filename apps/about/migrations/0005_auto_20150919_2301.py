# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20150919_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='meta_desc',
        ),
        migrations.RemoveField(
            model_name='about',
            name='meta_keys',
        ),
    ]
