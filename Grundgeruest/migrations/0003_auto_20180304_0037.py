# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-04 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grundgeruest', '0002_profil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name': 'Nutzerprofil', 'verbose_name_plural': 'Profile'},
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='nutzer',
            new_name='user',
        ),
    ]
