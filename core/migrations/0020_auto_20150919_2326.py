# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150919_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='meta_desc',
            field=models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 SEO'),
        ),
    ]
