# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='field_size',
            field=models.IntegerField(default=3, max_length=1, choices=[(0, b'2 man'), (1, b'4 players'), (4, b'16 players'), (3, b'32 players'), (4, b'64 players')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='game',
            field=models.IntegerField(default=0, max_length=1, choices=[(0, b'8-ball'), (1, b'9-ball'), (2, b'10-ball'), (3, b'One-pocket'), (4, b'Straight Pool'), (5, b'Bank Pool'), (6, b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='tourney_format',
            field=models.IntegerField(default=0, max_length=1, choices=[(0, b'Single elimination'), (1, b'Double elimination'), (2, b'Other')]),
            preserve_default=True,
        ),
    ]
