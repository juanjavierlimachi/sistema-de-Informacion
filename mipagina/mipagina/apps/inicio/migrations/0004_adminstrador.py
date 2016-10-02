# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0003_perfiles_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminstrador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ci', models.IntegerField(max_length=10)),
                ('telefono', models.IntegerField(max_length=8)),
                ('carrera', models.ForeignKey(to='carrera.carrera')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
