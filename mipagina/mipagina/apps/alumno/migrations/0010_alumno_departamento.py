# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0009_tribunal_grado'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='departamento',
            field=models.CharField(default='Pt', max_length=50),
            preserve_default=False,
        ),
    ]
