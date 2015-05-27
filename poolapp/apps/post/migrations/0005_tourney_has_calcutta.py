# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20150526_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='has_calcutta',
            field=models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
