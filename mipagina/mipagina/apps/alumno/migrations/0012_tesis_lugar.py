# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0011_remove_tesis_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='lugar',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
