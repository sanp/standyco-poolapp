# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_tourney_green_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='added_money_based_on_full_field',
            field=models.BooleanField(default=True, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
