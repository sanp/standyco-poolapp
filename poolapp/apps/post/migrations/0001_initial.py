# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourney',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pool_hall', models.CharField(max_length=200)),
                ('game', models.CharField(max_length=1, choices=[(1, b'8-ball'), (2, b'9-ball'), (3, b'10-ball'), (4, b'One-pocket'), (5, b'Straight Pool'), (6, b'Bank Pool'), (7, b'Other')])),
                ('field_size', models.CharField(max_length=1, choices=[(1, b'2 man'), (2, b'4 players'), (3, b'16 players'), (4, b'32 players'), (5, b'64 players')])),
                ('date', models.DateTimeField(verbose_name=b'Tournament Date')),
                ('fee', models.DecimalField(max_digits=6, decimal_places=2)),
                ('added_money', models.DecimalField(max_digits=6, decimal_places=2)),
                ('tourney_format', models.CharField(max_length=1, choices=[(1, b'Single elimination'), (2, b'Double elimination'), (3, b'Other')])),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=100)),
                ('start_time', models.TimeField(verbose_name=b'Start time')),
                ('end_time', models.TimeField(verbose_name=b'End time', blank=True)),
                ('title', models.CharField(max_length=70)),
                ('adtnl_info', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
