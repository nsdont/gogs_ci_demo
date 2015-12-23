# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('text', models.CharField(max_length=32, default='')),
            ],
        ),
    ]
