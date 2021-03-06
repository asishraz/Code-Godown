# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-06 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger_app', '0002_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
