# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=32, verbose_name='标题')),
                ('blogAuthor', models.CharField(max_length=16, verbose_name='作者')),
                ('blogReleasedTime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('blogContext', models.TextField(verbose_name='博客内容')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentContext', models.TextField(max_length=200, verbose_name='评论内容')),
                ('commentReleasedTime', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='博客')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标签')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]
