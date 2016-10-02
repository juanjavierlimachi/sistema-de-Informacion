# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0002_carrera_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(unique=True, max_length=150)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=250)),
                ('archivo', models.FileField(upload_to=b'documents')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(to='carrera.categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
