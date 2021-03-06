# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('votes', models.IntegerField()),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
