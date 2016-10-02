# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0006_mension'),
        ('alumno', '0013_auto_20160915_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='mension',
            field=models.ForeignKey(blank=True, to='carrera.mension', null=True),
            preserve_default=True,
        ),
    ]
