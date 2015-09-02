# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20150902_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='cover',
            field=models.ImageField(default='', upload_to=b'groups/', verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groups',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c'),
            preserve_default=True,
        ),
    ]
