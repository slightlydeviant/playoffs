# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncaaf', '0002_auto_20150206_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='ruleFormat',
        ),
        migrations.RemoveField(
            model_name='league',
            name='sportId',
        ),
        migrations.RemoveField(
            model_name='leagueusers',
            name='leagueId',
        ),
        migrations.DeleteModel(
            name='League',
        ),
        migrations.RemoveField(
            model_name='leagueusers',
            name='userId',
        ),
        migrations.DeleteModel(
            name='LeagueUsers',
        ),
        migrations.DeleteModel(
            name='Rules',
        ),
        migrations.DeleteModel(
            name='Sports',
        ),
    ]
