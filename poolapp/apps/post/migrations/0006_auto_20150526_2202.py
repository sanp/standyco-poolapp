# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_tourney_has_calcutta'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='race_to_a',
            field=models.IntegerField(null=True, verbose_name=b'Race to on A-Side', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourney',
            name='race_to_b',
            field=models.IntegerField(null=True, verbose_name=b'Race to on B-Side', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourney',
            name='race_to_single',
            field=models.IntegerField(null=True, verbose_name=b'Race to', blank=True),
            preserve_default=True,
        ),
    ]
