# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_20160820_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiles',
            old_name='cargo',
            new_name='carrera',
        ),
    ]
