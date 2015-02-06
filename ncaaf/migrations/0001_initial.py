# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ncaafGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('espnName', models.CharField(max_length=80)),
                ('displayName', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ncaafMatchups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.CharField(max_length=40)),
                ('gameId', models.ForeignKey(to='ncaaf.ncaafGame')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ncaafTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('espnName', models.CharField(max_length=80)),
                ('displayName', models.CharField(max_length=80)),
                ('displayInitial', models.CharField(max_length=2)),
                ('displayInitial2', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ncaafmatchups',
            name='homeTeam',
            field=models.ForeignKey(related_name='homeTeam', to='ncaaf.ncaafTeam', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ncaafmatchups',
            name='visitTeam',
            field=models.ForeignKey(related_name='visitTeam', to='ncaaf.ncaafTeam', null=True),
            preserve_default=True,
        ),
    ]
