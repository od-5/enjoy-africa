# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20150922_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='meta_desc',
            field=models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 SEO', blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='meta_keys',
            field=models.TextField(null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='meta_title',
            field=models.CharField(max_length=150, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a SEO', blank=True),
        ),
    ]
