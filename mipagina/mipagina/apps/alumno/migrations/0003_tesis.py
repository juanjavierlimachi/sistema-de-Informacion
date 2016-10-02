# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0006_mension'),
        ('alumno', '0002_tribunal'),
    ]

    operations = [
        migrations.CreateModel(
            name='tesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('numero_documento', models.CharField(max_length=50)),
                ('feche_dafensa', models.DateField()),
                ('hora_de_la_defensa', models.TimeField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('alumno', models.ForeignKey(to='alumno.Alumno')),
                ('carrera', models.ForeignKey(to='carrera.carrera')),
                ('tribunal', models.ManyToManyField(to='alumno.Tribunal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
