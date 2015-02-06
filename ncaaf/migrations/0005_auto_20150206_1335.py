# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ncaaf', '0004_auto_20150206_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='Password',
            new_name='password',
        ),
        migrations.AddField(
            model_name='league',
            name='creator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
