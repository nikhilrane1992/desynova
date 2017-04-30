# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desynova', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasteLockly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_url_string', models.CharField(unique=True, max_length=100)),
                ('secret_key', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Short_url',
            new_name='ShortUrl',
        ),
        migrations.RenameField(
            model_name='shorturl',
            old_name='short_random_string',
            new_name='short_url_string',
        ),
    ]
