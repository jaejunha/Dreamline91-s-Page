# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamline91', '0007_auto_20180111_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Happy',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=100)),
            ],
        ),
    ]
