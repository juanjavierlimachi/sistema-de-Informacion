from django import forms
from django.forms import ModelForm
from .models import *

class CarreraForm(ModelForm):
	class Meta:
		model=carrera
		exclude=('estado',)

class CategoriaForm(ModelForm):
	class Meta:
		model=categoria
		exclude=('estado',)		

class NoticiaForm(ModelForm):
	class Meta:
		model=Noticia
		exclude=('estado','usuario')

class NoticiaFormDir(ModelForm):
	class Meta:
		model=Noticia
		exclude=('estado','carrera','usuario',)
class MencionForm(ModelForm):
	class Meta:
		model=mension
		exclude=('estado',)
