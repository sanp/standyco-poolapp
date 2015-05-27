# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20150526_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='green_fees_included',
            field=models.BooleanField(default=True, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
