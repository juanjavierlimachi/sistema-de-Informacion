# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0006_mension'),
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tribunal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('carrera', models.ForeignKey(to='carrera.carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
