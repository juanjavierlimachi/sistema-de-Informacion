# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_auto_20160820_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_cargo', models.CharField(unique=True, max_length=100)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='adminstrador',
            name='carrera',
        ),
        migrations.AddField(
            model_name='adminstrador',
            name='cargo',
            field=models.ForeignKey(default='1', to='inicio.cargo'),
            preserve_default=False,
        ),
    ]
