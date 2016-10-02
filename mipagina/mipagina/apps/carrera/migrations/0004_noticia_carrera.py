# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0003_categoria_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='carrera',
            field=models.ForeignKey(default=1, to='carrera.carrera'),
            preserve_default=False,
        ),
    ]
