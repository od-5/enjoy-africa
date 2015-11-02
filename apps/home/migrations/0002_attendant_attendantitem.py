# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0448 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0430\u044e\u0449\u0438\u0439',
                'verbose_name_plural': '\u041d\u0430\u0448 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0430\u044e\u0449\u0438\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttendantItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('icon', models.CharField(default=b'block5-icon-browser', max_length=50, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430', choices=[(b'block5-icon-browser', '\u041a\u043e\u043c\u043f\u0430\u0441'), (b'block5-icon-aircraft', '\u0421\u0430\u043c\u043e\u043b\u0451\u0442'), (b'block5-icon-umbrella', '\u0417\u043e\u043d\u0442\u0438\u043a'), (b'block5-icon-camera', '\u041a\u0430\u043c\u0435\u0440\u0430')])),
                ('attendant', models.ForeignKey(to='home.Attendant')),
            ],
            options={
                'verbose_name': '\u041f\u0443\u043d\u043a\u0442',
                'verbose_name_plural': '\u041f\u0443\u043d\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
