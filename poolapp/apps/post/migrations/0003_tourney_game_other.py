# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150521_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='game_other',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Other Game', blank=True),
            preserve_default=True,
        ),
    ]
