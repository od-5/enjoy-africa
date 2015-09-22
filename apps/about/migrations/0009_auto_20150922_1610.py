# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20150922_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='meta_desc',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 SEO', blank=True),
        ),
    ]
