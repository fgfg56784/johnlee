# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-05 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='q',
            new_name='question',
        ),
    ]
