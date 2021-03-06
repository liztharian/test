# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-02 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180801_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
