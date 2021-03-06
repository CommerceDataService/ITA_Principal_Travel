# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 14:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0011_auto_20160323_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 24, 14, 42, 54, 947478, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='edited_on',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 24, 14, 43, 8, 329793, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='principal',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 24, 14, 43, 19, 848390, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='principal',
            name='edited_on',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 24, 14, 43, 28, 258415, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 24, 14, 43, 52, 975882, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='edited_on',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 24, 14, 44, 4, 482384, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
