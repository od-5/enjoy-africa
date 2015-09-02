# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_travelreviewcomment'),
        ('core', '0015_remove_avatar_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('description', ckeditor.fields.RichTextField(max_length=255, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('reserved', models.PositiveIntegerField(default=0, verbose_name='\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043e \u043c\u0435\u0441\u0442')),
                ('seats', models.PositiveIntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442')),
                ('travel_start', models.DateField(null=True, verbose_name='\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u0435', blank=True)),
                ('travel_end', models.DateField(null=True, verbose_name='\u041e\u0442\u044a\u0435\u0437\u0434', blank=True)),
                ('travel', models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', to='travel.Travel')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b',
            },
            bases=('core.common',),
        ),
        migrations.CreateModel(
            name='GroupTicket',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('email', models.EmailField(max_length=256, verbose_name='e-mail')),
                ('comment', models.TextField(null=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430', blank=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438',
            },
            bases=('core.common',),
        ),
    ]
