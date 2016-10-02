# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0010_alumno_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesis',
            name='carrera',
        ),
    ]
