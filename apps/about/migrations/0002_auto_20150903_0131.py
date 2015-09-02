# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-created'], 'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
    ]
