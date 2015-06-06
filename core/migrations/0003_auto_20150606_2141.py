# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('image', models.ImageField(upload_to=b'top_slider', verbose_name='\u0421\u043b\u0430\u0439\u0434')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='setup',
            name='meta_desc',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 META_DESCRIPTION', blank=True),
        ),
        migrations.AlterField(
            model_name='setup',
            name='meta_key',
            field=models.TextField(verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 META_KEYWORDS', blank=True),
        ),
        migrations.AlterField(
            model_name='setup',
            name='title',
            field=models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a <TITLE>...</TITLE>', blank=True),
        ),
    ]
