# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_auto_20150907_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'ordering': ['-travel_start'], 'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b'},
        ),
    ]
