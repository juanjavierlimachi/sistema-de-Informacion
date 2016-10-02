# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0006_mension'),
        ('alumno', '0014_tesis_mension'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='carrera',
            field=models.ForeignKey(default=1, to='carrera.carrera'),
            preserve_default=False,
        ),
    ]
