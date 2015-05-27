# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_tourney_added_money_based_on_full_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourney',
            name='end_time',
        ),
        migrations.AddField(
            model_name='tourney',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'End Date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourney',
            name='multiple_days',
            field=models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
