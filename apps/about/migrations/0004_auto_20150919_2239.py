# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='description',
            new_name='meta_desc',
        ),
        migrations.AddField(
            model_name='about',
            name='meta_keys',
            field=models.CharField(max_length=500, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430'),
            preserve_default=True,
        ),
    ]
