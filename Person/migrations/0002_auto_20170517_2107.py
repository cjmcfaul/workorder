# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor_typer',
            new_name='vendor_type',
        ),
    ]
