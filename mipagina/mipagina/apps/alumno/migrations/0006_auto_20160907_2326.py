# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0005_auto_20160907_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tesis',
            old_name='feche_dafensa',
            new_name='fecha_de_defensa',
        ),
    ]
