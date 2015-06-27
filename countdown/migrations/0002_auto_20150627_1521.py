# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430'),
        ),
    ]
