# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupticket',
            name='common_ptr',
        ),
        migrations.DeleteModel(
            name='GroupTicket',
        ),
    ]
