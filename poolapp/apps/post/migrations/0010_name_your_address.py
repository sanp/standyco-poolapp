# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='your_address',
            field=models.CharField(default='222 West Street', max_length=100),
            preserve_default=False,
        ),
    ]
