# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_tourney_green_fees_included'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='green_fees',
            field=models.IntegerField(null=True, verbose_name=b'Green Fees', blank=True),
            preserve_default=True,
        ),
    ]
