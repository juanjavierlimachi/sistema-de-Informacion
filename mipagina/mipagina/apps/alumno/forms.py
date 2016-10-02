#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *
gra = (('Ing', 'Ingeniero(a)',), ('Lic', 'Licenciado(a)',))
class TribunalForm(ModelForm):
	grado=forms.ChoiceField(widget=forms.Select, choices=gra)
	class Meta:
		model=Tribunal
		exclude=('estado',)
tipo = (('Proyecto de Grado', 'Proyecto de Grado',), ('Tesis', 'Tesis',),('Exelencia', 'Exelencia',),('Años de Experiencia','Años de Experiencia',))
class TesisForm(ModelForm):
	modaliad=forms.ChoiceField(widget=forms.Select, choices=tipo)
	class Meta:
		model=tesis
		exclude=('estado','tribunal','hora_de_Conclucion','calificacion','alumno','modalidad',)
calificacion = (('Aprobado','Aprobado',),('Simplemente Aprobado', 'Simplemente Aprobado',), ('Aprobado con Felicitaciones', 'Aprobado con Felicitaciones',),('APROBADO CON HONORES','APROBADO CON HONORES',))
class TribunalFormAdd(forms.Form):
	tribunal_1 = forms.CharField(max_length=150,required=True, label="Tribunal 1")
	tribunal_2 = forms.CharField(max_length=150,required=True, label="Tribunal 2")
	tribunal_3 = forms.CharField(max_length=150,required=True, label="Tribunal 2")
	hora = forms.CharField(max_length=15, required=True)
	calificacion = forms.ChoiceField(widget=forms.Select, choices=calificacion)
dep = (('Pt.', 'PT',), ('Lp.', 'LP',),('Or.', 'OR',), ('Cb.', 'CB',),('Ch.', 'CH',), ('Tj.', 'TJ',),('Pa.', 'PA',), ('Be.', 'BE',))
sex = (('M', 'Masculino',), ('F', 'Femenino',))
class AlumnoForm(ModelForm):
	nombre = forms.CharField(max_length = 100)
	departamento=forms.ChoiceField(widget=forms.Select, choices=dep)
	sexo=forms.ChoiceField(widget=forms.Select, choices=sex)
	class Meta:
		model=Alumno
		exclude=('estado','usuario','carrera',)

class formulariotesis(ModelForm):
	class Meta:
		model=tesis
		exclude=('estado','tribunal','hora_de_Conclucion','calificacion','alumno','modaliad','mension','carrera',)
class Updateformtesis(ModelForm):
	class Meta:
		model=tesis
		exclude=('estado','tribunal','hora_de_Conclucion','calificacion','alumno','modaliad','mension','carrera',)