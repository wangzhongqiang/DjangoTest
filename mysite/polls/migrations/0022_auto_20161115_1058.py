# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20161115_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boy1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mama1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('boys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Boy1')),
            ],
        ),
        migrations.RemoveField(
            model_name='mama',
            name='boys',
        ),
        migrations.DeleteModel(
            name='Boy',
        ),
        migrations.DeleteModel(
            name='Mama',
        ),
    ]