# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20150409_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourney',
            name='id',
        ),
        migrations.AddField(
            model_name='tourney',
            name='tourney_id',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
