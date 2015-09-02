# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20150903_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='url', blank=True),
            preserve_default=False,
        ),
    ]
