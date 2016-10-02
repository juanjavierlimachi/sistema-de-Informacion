# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiles',
            name='telefono',
            field=models.IntegerField(default=999999, max_length=8),
            preserve_default=False,
        ),
    ]
