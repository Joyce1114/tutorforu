# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor4u', '0002_auto_20161120_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='course2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='course3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='grade1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='grade2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='grade3',
            field=models.CharField(default='', max_length=200),
        ),
    ]