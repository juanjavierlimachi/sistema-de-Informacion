from django.db import models
from django.contrib.auth.forms import User
from mipagina.apps.carrera.models import *

# Create your models here.
#Este modelo es el Perfil del Director de la facultad de ing
class Perfiles(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfil')
	ci = models.IntegerField(max_length=10)
	telefono = models.IntegerField(max_length=8)
	carrera = models.ForeignKey(carrera)
	def __unicode__(self):
		return self.usuario.username
#est modelo es el administrador quien registra a los directores de cada carrera ejem(secretaria. labarotorios)
class cargo(models.Model):
	nombre_cargo=models.CharField(max_length=100,unique=True)
	fecha=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.nombre_cargo
#Este modelo es Modulo secretaria
class adminstrador(models.Model):
	usuario = models.OneToOneField(User, unique=True)
	ci = models.IntegerField(max_length=10)
	telefono=models.IntegerField(max_length=8)
	cargo=models.ForeignKey(cargo)
	carrera=models.ForeignKey(carrera)
	def __unicode__(self):
		return self.usuario.username



