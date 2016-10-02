# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0004_auto_20160906_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='calificacion',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tesis',
            name='hora_de_Conclucion',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
