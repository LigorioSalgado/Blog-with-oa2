# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-16 01:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_cliente',
            new_name='id_usuario',
        ),
    ]
