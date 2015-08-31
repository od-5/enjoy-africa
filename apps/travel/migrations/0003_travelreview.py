# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20150830_1912'),
        ('travel', '0002_travel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelReview',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(upload_to=b'travels/', verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430')),
                ('text', ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('moderated', models.BooleanField(default=False, verbose_name='\u041e\u0434\u043e\u0431\u0440\u0435\u043d\u043e')),
                ('slug', models.SlugField(max_length=100, verbose_name='url', blank=True)),
                ('travel', models.ForeignKey(verbose_name='\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', to='travel.Travel')),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
            bases=('core.common',),
        ),
    ]
