# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0006_auto_20160907_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(default='M', max_length=100),
            preserve_default=False,
        ),
    ]
