# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_themequestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Blog'),
        ),
    ]
