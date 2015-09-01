# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150831_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='description',
            field=models.CharField(default='\u0410\u0432\u0442\u043e\u0440', max_length=255, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(upload_to=b'profile/', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
        ),
    ]
