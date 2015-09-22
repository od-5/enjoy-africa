# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_title', models.CharField(max_length=150, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a SEO', blank=True)),
                ('meta_desc', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 SEO', blank=True)),
                ('meta_keys', models.TextField(null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True)),
                ('page', models.CharField(unique=True, max_length=100, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430', choices=[(b'about', '\u041e \u043d\u0430\u0441'), (b'travel', '\u0416\u0443\u0440\u043d\u0430\u043b \u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u0439'), (b'groups', '\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0435 \u0442\u0443\u0440\u044b'), (b'forum', '\u0424\u043e\u0440\u0443\u043c')])),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=(models.Model,),
        ),
    ]
