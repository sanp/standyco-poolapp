# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_name_your_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='id',
        ),
        migrations.AddField(
            model_name='name',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
