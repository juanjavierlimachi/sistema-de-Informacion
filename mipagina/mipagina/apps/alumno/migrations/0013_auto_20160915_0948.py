# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0012_tesis_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesis',
            name='alumno',
            field=models.OneToOneField(to='alumno.Alumno'),
        ),
    ]
