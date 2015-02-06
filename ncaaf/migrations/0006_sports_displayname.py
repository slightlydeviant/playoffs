# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncaaf', '0005_auto_20150206_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='displayName',
            field=models.CharField(default='College Football', max_length=80),
            preserve_default=False,
        ),
    ]
