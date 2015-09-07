# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_groupticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c', blank=True),
            preserve_default=True,
        ),
    ]
