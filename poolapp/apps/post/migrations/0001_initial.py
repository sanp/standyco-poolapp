# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourney',
            fields=[
                ('tourney_id', models.AutoField(serialize=False, primary_key=True)),
                ('state', localflavor.us.models.USStateField(default=b'IL', max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('pool_hall', models.CharField(max_length=200)),
                ('game', models.IntegerField(default=0, choices=[(0, b'8-ball'), (1, b'9-ball'), (2, b'10-ball'), (3, b'One-pocket'), (4, b'Straight Pool'), (5, b'Bank Pool'), (6, b'Other')])),
                ('field_size', models.IntegerField(default=3, choices=[(0, b'2 man'), (1, b'4 players'), (4, b'16 players'), (3, b'32 players'), (4, b'64 players')])),
                ('date', models.DateField(verbose_name=b'Tournament Date')),
                ('fee', models.DecimalField(max_digits=6, decimal_places=2)),
                ('added_money', models.DecimalField(max_digits=6, decimal_places=2)),
                ('tourney_format', models.IntegerField(default=0, choices=[(0, b'Single elimination'), (1, b'Double elimination'), (2, b'Other')])),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact_email', models.EmailField(max_length=100)),
                ('start_time', models.TimeField(verbose_name=b'Start time')),
                ('end_time', models.TimeField(null=True, verbose_name=b'End time', blank=True)),
                ('title', models.CharField(max_length=70)),
                ('adtnl_info', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
