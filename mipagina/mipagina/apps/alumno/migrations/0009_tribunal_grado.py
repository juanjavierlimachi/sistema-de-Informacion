# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0008_tesis_modaliad'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribunal',
            name='grado',
            field=models.CharField(default='Ing', max_length=50),
            preserve_default=False,
        ),
    ]
