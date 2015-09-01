# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150901_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='description',
        ),
    ]
