# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_tourney_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='adtnl_info',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
