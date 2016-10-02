# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0005_noticia_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='mension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mension', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('carrera', models.ForeignKey(to='carrera.carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
