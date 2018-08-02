# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-02 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grundgeruest', '0003_auto_20180304_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kommentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('zeit_geaendert', models.DateTimeField(auto_now=True)),
                ('nutzer_geaendert', models.TextField(default='0', editable=False)),
                ('text', martor.models.MartorField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kommentare', to='Grundgeruest.Profil')),
            ],
            options={
                'verbose_name': 'Kommentar',
                'verbose_name_plural': 'Kommentare',
            },
        ),
        migrations.CreateModel(
            name='Liste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('zeit_geaendert', models.DateTimeField(auto_now=True)),
                ('nutzer_geaendert', models.TextField(default='0', editable=False)),
            ],
            options={
                'verbose_name': 'Kommentarliste',
                'verbose_name_plural': 'Kommentarlisten',
            },
        ),
        migrations.AddField(
            model_name='kommentar',
            name='liste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kommentare', to='Kommentare.Liste'),
        ),
    ]
