# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-29 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_article',
            name='image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]