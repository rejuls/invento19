# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-27 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20180226_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
