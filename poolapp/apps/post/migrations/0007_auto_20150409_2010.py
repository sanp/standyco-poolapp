# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20150409_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='adtnl_info',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='end_time',
            field=models.TimeField(null=True, verbose_name=b'End time', blank=True),
            preserve_default=True,
        ),
    ]
