# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_common_meta_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='robots_txt',
            field=models.TextField(null=True, verbose_name='robots.txt', blank=True),
            preserve_default=True,
        ),
    ]
