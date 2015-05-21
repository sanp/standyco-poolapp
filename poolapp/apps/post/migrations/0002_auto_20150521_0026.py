# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='fee',
            field=models.DecimalField(verbose_name=b'Entry Fee', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='pool_hall',
            field=models.CharField(max_length=200, verbose_name=b'Location'),
            preserve_default=True,
        ),
    ]
