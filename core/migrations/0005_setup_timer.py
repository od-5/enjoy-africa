# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='timer',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u0434 \u0442\u0430\u0439\u043c\u0435\u0440\u0430', blank=True),
            preserve_default=True,
        ),
    ]
