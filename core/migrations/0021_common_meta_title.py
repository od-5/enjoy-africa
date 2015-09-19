# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150919_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='common',
            name='meta_title',
            field=models.CharField(max_length=150, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a SEO'),
            preserve_default=True,
        ),
    ]
