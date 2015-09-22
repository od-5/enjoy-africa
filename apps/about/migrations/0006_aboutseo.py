# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20150922_1235'),
        ('about', '0005_auto_20150919_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSEO',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
            ],
            options={
            },
            bases=('core.common',),
        ),
    ]
