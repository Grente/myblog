# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-03 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=16, verbose_name='\u4f5c\u8005')),
                ('content', models.TextField(default='', verbose_name='\u6b63\u6587')),
                ('create_time', models.DateField(auto_now=True, verbose_name='\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6211\u7684\u535a\u5ba2',
                'verbose_name_plural': '\u6211\u7684\u535a\u5ba2',
            },
        ),
    ]
