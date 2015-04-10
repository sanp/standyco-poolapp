# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150409_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='date',
            field=models.DateField(verbose_name=b'Tournament Date'),
            preserve_default=True,
        ),
    ]
