# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ticket_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setup',
            name='timer',
        ),
        migrations.AddField(
            model_name='setup',
            name='video',
            field=models.TextField(null=True, verbose_name='HTML-\u043a\u043e\u0434 \u0432\u0438\u0434\u0435\u043e', blank=True),
            preserve_default=True,
        ),
    ]
