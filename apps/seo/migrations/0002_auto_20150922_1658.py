# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', choices=[(b'about', '\u041e \u043d\u0430\u0441'), (b'travel', '\u0416\u0443\u0440\u043d\u0430\u043b \u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u0439'), (b'groups', '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b'), (b'forum', '\u0424\u043e\u0440\u0443\u043c')]),
        ),
    ]
