# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_perfiles_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiles',
            name='cargo',
            field=models.CharField(default='secretatio', max_length=50),
            preserve_default=False,
        ),
    ]
