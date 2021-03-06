# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConcertifyApi', '0004_concert_mainhall_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentID', models.FloatField(default=0)),
                ('commentOwner', models.CharField(blank=True, default='', max_length=36)),
                ('content', models.CharField(blank=True, default='', max_length=500)),
                ('voteCount', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('voteCount',),
            },
        ),
    ]
