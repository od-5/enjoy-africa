# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20150903_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
