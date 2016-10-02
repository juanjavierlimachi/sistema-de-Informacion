# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0007_alumno_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='modaliad',
            field=models.CharField(default='Tesis', max_length=100),
            preserve_default=False,
        ),
    ]
