from django.db import models
from django.contrib.auth.forms import User
# Create your models here.
class carrera(models.Model):
	carrera=models.CharField(max_length=50)
	fecha_registro=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.carrera

class categoria(models.Model):
	categoria=models.CharField(max_length=150,unique=True)
	fecha=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.categoria

class mension(models.Model):
	mension=models.CharField(max_length=50)
	carrera=models.ForeignKey(carrera)
	fecha=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.mension

class Noticia(models.Model):
	titulo=models.CharField(max_length=50)
	texto=models.TextField(max_length=250)
	archivo=models.FileField(upload_to = 'documents')
	carrera=models.ForeignKey(carrera)
	categoria=models.ForeignKey(categoria)
	usuario=models.ForeignKey(User)
	fecha=models.DateTimeField(auto_now=True)
	estado=models.IntegerField(default=0)
	def __unicode__(self):
		return self.titulo

