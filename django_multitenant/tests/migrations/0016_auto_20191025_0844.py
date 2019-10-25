# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-25 08:44
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0015_auto_20190829_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmanager',
            name='project',
            field=django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectmanagers', to='tests.Project'),
        ),
    ]
