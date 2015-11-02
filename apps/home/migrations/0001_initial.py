# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block10',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('icon', models.CharField(default=b'block10-icon-1', max_length=50, choices=[(b'block10-icon-1', '\u0441\u0430\u043c\u043e\u043b\u0451\u0442'), (b'block10-icon-2', '\u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c'), (b'block10-icon-3', '\u0434\u043e\u043c'), (b'block10-icon-4', '\u0433\u0438\u0434'), (b'block10-icon-6', '\u043c\u0435\u0433\u0430\u0444\u043e\u043d'), (b'block10-icon-7', '\u043c\u043e\u043d\u0435\u0442\u044b'), (b'block10-icon-8', '\u0431\u0443\u0442\u044b\u043b\u043a\u0430'), (b'block10-icon-9', '\u0441\u0438\u043c \u043a\u0430\u0440\u0442\u0430')])),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0427\u0442\u043e \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043e \u0432 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u0427\u0442\u043e \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043e \u0432 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Block3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('icon', models.CharField(default=b'block3-icon-posr', max_length=50, choices=[(b'block3-icon-posr', '\u043b\u044e\u0434\u0438'), (b'block3-icon-24h', '24 \u0447\u0430\u0441\u0430'), (b'block3-icon-zvuk', '\u043c\u0435\u0433\u0430\u0444\u043e\u043d'), (b'block3-icon-money', '\u043c\u043e\u043d\u0435\u0442\u044b')])),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0447\u0435\u043c\u0443 \u0438\u043c\u0435\u043d\u043d\u043e \u043c\u044b',
                'verbose_name_plural': '\u041f\u043e\u0447\u0435\u043c\u0443 \u0438\u043c\u0435\u043d\u043d\u043e \u043c\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('block', models.PositiveSmallIntegerField(default=1, unique=True, choices=[(1, '\u041f\u0435\u0440\u0432\u044b\u0439 \u0431\u043b\u043e\u043a'), (2, '\u041f\u043e\u0447\u0435\u043c\u0443 \u0438\u043c\u0435\u043d\u043d\u043e \u043c\u044b'), (3, '\u041f\u0435\u0440\u0432\u0430\u044f \u0444\u043e\u0440\u043c\u0430 \u0441 \u0437\u0430\u044f\u0432\u043a\u043e\u0439'), (4, '\u0421\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0430\u044e\u0449\u0438\u0439'), (5, '4 \u0448\u0430\u0433\u0430'), (6, '\u041f\u0435\u0440\u0432\u044b\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a'), (7, '\u0427\u0442\u043e \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043e \u0432 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c'), (8, '\u0412\u0442\u043e\u0440\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a'), (9, '\u041e\u0442\u0437\u044b\u0432\u044b \u043e \u043f\u043e\u0435\u0437\u0434\u043a\u0430\u0445')])),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430',
                'verbose_name_plural': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0431\u043b\u043e\u043a\u043e\u0432',
            },
            bases=(models.Model,),
        ),
    ]
