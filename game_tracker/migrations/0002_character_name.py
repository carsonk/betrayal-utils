# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
