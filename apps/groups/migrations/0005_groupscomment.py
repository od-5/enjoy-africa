# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_ticket_group'),
        ('groups', '0004_groups_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupsComment',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('text', ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('groups', models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0439 \u0442\u0443\u0440', to='groups.Groups')),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
            bases=('core.common',),
        ),
    ]
