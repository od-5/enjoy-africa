# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430')),
                ('cycle', models.BooleanField(default=True, verbose_name='\u0417\u0430\u0446\u0438\u043a\u043b\u0438\u0442\u044c')),
                ('offset', models.PositiveIntegerField(default=14, verbose_name='\u041a\u043e\u043b-\u0432\u043e \u0434\u043d\u0435\u0439')),
            ],
            options={
                'verbose_name': '\u0422\u0430\u0439\u043c\u0435\u0440 \u043e\u0431\u0440\u0430\u0431\u0442\u043d\u043e\u0433\u043e \u043e\u0442\u0441\u0447\u0451\u0442\u0430',
                'verbose_name_plural': '\u0422\u0430\u0439\u043c\u0435\u0440 \u043e\u0431\u0440\u0430\u0431\u0442\u043d\u043e\u0433\u043e \u043e\u0442\u0441\u0447\u0451\u0442\u0430',
            },
            bases=(models.Model,),
        ),
    ]
