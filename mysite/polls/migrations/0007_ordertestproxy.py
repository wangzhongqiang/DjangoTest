# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 10:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_mytestproxy_testproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTestProxy',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
            },
            bases=('polls.testproxy',),
        ),
    ]