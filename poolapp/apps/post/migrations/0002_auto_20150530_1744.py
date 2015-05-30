# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourney',
            name='date',
        ),
        migrations.AddField(
            model_name='tourney',
            name='city',
            field=models.CharField(default='Some city', max_length=200, verbose_name=b'City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourney',
            name='start_date',
            field=models.DateField(default='2015-05-09', verbose_name=b'Start Date'),
            preserve_default=False,
        ),
    ]
