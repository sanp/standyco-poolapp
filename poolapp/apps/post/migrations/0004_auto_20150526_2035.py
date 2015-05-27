# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_tourney_game_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='field_size_other',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Other Field Size', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourney',
            name='tourney_format_other',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Other Format', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='field_size',
            field=models.IntegerField(default=3, choices=[(0, b'2 man'), (1, b'4 players'), (4, b'16 players'), (3, b'32 players'), (4, b'64 players'), (5, b'Other')]),
            preserve_default=True,
        ),
    ]
