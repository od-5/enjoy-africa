# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_groupscomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupscomment',
            name='common_ptr',
        ),
        migrations.RemoveField(
            model_name='groupscomment',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='groupscomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='GroupsComment',
        ),
    ]
