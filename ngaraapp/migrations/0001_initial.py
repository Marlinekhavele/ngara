# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-02 14:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
