# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0002_auto_20150627_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='text',
            field=models.TextField(default='', verbose_name='\u0422\u0435\u043a\u0441\u0442'),
            preserve_default=False,
        ),
    ]
