# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_setup_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='comment',
            field=models.TextField(null=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
