# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150713_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438', blank=True, choices=[(0, '\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435'), (1, '\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430'), (2, '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430'), (3, '\u041d\u0435\u0442 \u043e\u0442\u0432\u0435\u0442\u0430')]),
        ),
    ]
