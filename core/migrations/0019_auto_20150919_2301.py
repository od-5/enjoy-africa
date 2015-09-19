# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_avatar_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='common',
            name='meta_desc',
            field=models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='common',
            name='meta_keys',
            field=models.CharField(max_length=500, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430'),
            preserve_default=True,
        ),
    ]
