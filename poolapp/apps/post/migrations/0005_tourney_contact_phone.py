# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_tourney_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
    ]
