# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_tesis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesis',
            name='tribunal',
            field=models.ManyToManyField(to=b'alumno.Tribunal', null=True, blank=True),
        ),
    ]
