from django.db import models
from mipagina.apps.carrera.models import *
# Create your models here.

class Alumno(models.Model):
	nombre=models.CharField(max_length=100)
	apellido_paterno=models.CharField(max_length=100)
	apellido_materno=models.CharField(max_length=100)
	sexo=models.CharField(max_length=100)
	ci=models.IntegerField(max_length=9)
	departamento=models.CharField(max_length=50)
	carrera=models.ForeignKey(carrera)
	usuario=models.ForeignKey(User)
	fecha=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return "%s %s %s"%(self.nombre,self.apellido_paterno,self.apellido_materno)

class Tribunal(models.Model):
	nombre=models.CharField(max_length=100)
	apellido_paterno=models.CharField(max_length=100)
	apellido_materno=models.CharField(max_length=100)
	carrera=models.ForeignKey(carrera)
	grado=models.CharField(max_length=50)
	fecha=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return "%s %s %s %s"%(self.nombre,self.apellido_paterno,self.apellido_materno,self.carrera)

class tesis(models.Model):
	titulo=models.CharField(max_length=250)
	mension=models.ForeignKey(mension, null=True, blank=True)
	modaliad=models.CharField(max_length=100)
	alumno=models.OneToOneField(Alumno)
	carrera=models.ForeignKey(carrera)
	numero_documento=models.CharField(max_length=50)
	tribunal=models.ManyToManyField(Tribunal, null=True, blank=True)
	fecha_de_defensa=models.DateField()
	hora_de_la_defensa=models.TimeField()
	lugar=models.CharField(max_length=100)
	fecha_registro=models.DateTimeField(auto_now=True)
	hora_de_Conclucion=models.TimeField(null=True, blank=True)
	calificacion=models.CharField(max_length=50, null=True, blank=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.titulo
