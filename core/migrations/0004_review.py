# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150606_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('photo', models.ImageField(upload_to=b'review', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('content', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=('core.common',),
        ),
    ]
