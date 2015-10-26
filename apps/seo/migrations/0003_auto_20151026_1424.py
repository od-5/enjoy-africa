# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_auto_20150922_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=260, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', choices=[(b'about', '\u041e \u043d\u0430\u0441'), (b'travels', '\u0416\u0443\u0440\u043d\u0430\u043b \u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u0439'), (b'groups', '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b'), (b'forum', '\u0424\u043e\u0440\u0443\u043c')]),
        ),
    ]
