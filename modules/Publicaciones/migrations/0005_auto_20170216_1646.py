# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-16 22:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicaciones', '0004_publicacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL),
        ),
    ]
