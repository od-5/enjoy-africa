# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150627_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0430\u0436\u0430',
                'proxy': True,
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0430\u0436\u0438',
            },
            bases=('core.ticket',),
        ),
        migrations.AddField(
            model_name='ticket',
            name='commission',
            field=models.PositiveIntegerField(default=0, verbose_name='\u041a\u043e\u043c\u043c\u0438\u0441\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0421\u0443\u043c\u043c\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0440\u043e\u0434\u0430\u0436\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='sale_comment',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='sale_status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u0440\u043e\u0434\u0430\u0436\u0438', choices=[(0, '\u041e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 \u043e\u043f\u043b\u0430\u0442\u044b'), (1, '\u0423\u0442\u043e\u0447\u043d\u0435\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0435\u0439'), (2, '\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_comment',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438', choices=[(0, '\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435'), (1, '\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430'), (2, '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0418\u0442\u043e\u0433\u043e'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='travel_end',
            field=models.DateField(null=True, verbose_name='\u041a\u043e\u043d\u0435\u0446 \u0442\u0443\u0440\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='travel_start',
            field=models.DateField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u0442\u0443\u0440\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.TextField(null=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430', blank=True),
        ),
    ]
