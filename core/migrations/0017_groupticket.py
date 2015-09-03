# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_ticket_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTicket',
            fields=[
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430',
                'proxy': True,
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0437\u0430\u044f\u0432\u043a\u0438',
            },
            bases=('core.ticket',),
        ),
    ]
