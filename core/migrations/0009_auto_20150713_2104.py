# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150713_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='commission',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u041a\u043e\u043c\u043c\u0438\u0441\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u0421\u0443\u043c\u043c\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='total_price',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u0418\u0442\u043e\u0433\u043e', blank=True),
        ),
    ]
