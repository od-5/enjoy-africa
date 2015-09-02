# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20150902_2352'),
        ('core', '0015_remove_avatar_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='group',
            field=models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0439 \u0442\u0443\u0440', blank=True, to='groups.Groups', null=True),
            preserve_default=True,
        ),
    ]
