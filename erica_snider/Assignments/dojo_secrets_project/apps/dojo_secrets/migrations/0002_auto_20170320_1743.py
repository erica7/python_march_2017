# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_secrets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secret',
            old_name='text',
            new_name='secret',
        ),
    ]