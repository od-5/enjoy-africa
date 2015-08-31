# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150830_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('title', models.CharField(max_length=150, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f',
            },
            bases=('core.common',),
        ),
    ]
