# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_adminstrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='cargo',
            field=models.ForeignKey(to='carrera.carrera'),
        ),
    ]
