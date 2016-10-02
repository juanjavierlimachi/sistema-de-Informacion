# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0002_carrera_estado'),
        ('inicio', '0007_auto_20160820_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminstrador',
            name='carrera',
            field=models.ForeignKey(default=1, to='carrera.carrera'),
            preserve_default=False,
        ),
    ]
