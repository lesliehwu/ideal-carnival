# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]