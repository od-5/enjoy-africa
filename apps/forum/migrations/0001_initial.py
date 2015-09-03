# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_groupticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', ckeditor.fields.RichTextField(max_length=255, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('file', models.FileField(upload_to=b'forum/', null=True, verbose_name='\u0424\u0430\u0439\u043b', blank=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='url', blank=True)),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0422\u0435\u043c\u0430',
                'verbose_name_plural': '\u0422\u0435\u043c\u044b',
            },
            bases=('core.common',),
        ),
        migrations.CreateModel(
            name='ThemeComment',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('text', ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('theme', models.ForeignKey(verbose_name='\u0422\u0435\u043a\u0441\u0442', to='forum.Theme')),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
            bases=('core.common',),
        ),
    ]
