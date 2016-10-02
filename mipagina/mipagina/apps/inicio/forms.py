#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import User
from mipagina.apps.carrera.models import *
#tipo = (('secretaria', 'Secretario(a)',), ('laboratorio', 'Resp. de Laboratorio',),('secretaria', 'Secretario(a)',), ('laboratorio', 'Resp. de Laboratorio',))
class UserForm(UserCreationForm):
	username = forms.CharField(max_length=40,required=True,label="Nombre de Usuario")
	password1 = forms.CharField(required=True,label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(required=True, label="Confirmacion",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=40,required=True, label="Nombre Completo")
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=50,required=True, label="Apellido(s)")
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	ci = forms.IntegerField(required=True,label="Nro. de CI")
	telefono = forms.IntegerField(required=True,label="Telefono/Celular")
	carrera = forms.ModelChoiceField(queryset=carrera.objects.all())
	def clean_ci(self):
		ci=self.cleaned_data['ci']
		try:
			p=Perfiles.objects.get(ci=ci)
		except Perfiles.DoesNotExist:
			return ci
		raise forms.ValidationError('El Nro. de CI ya Existe')
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","email")
		widgets = {
			'password1':forms.PasswordInput(),
		}
	def save(self,commit=True):
		user=super(UserForm,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		if commit:
			user.save()
		return user
#formularios para editar el usuario
class formPerfiles(forms.ModelForm):
	class Meta:
		model=Perfiles
		exclude=['usuario','carrera']
class UserForms(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','first_name','last_name','email')
		#exclude=['password']

class CambioForm(forms.Form):
	Nueva_Contracenia= forms.CharField(required=True, label="Contracenia",widget=forms.PasswordInput(render_value=False))
	Confirmacion	 = forms.CharField(required=True, label="Confirmar",widget=forms.PasswordInput(render_value=False))
	def password(self):
		pass_one=self.cleaned_data['Nueva_Contracenia']
		pass_tho=self.cleaned_data['Confirmacion']
		if pass_one == pass_tho:
			pass
		else:
			raise forms.ValidationError('Los datos no Coinsiden')

#sub sistema Director
class UserFormPersonal(UserCreationForm):
	username = forms.CharField(max_length=40,required=True,label="Nombre de Usuario")
	password1 = forms.CharField(required=True,label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(required=True, label="Confirmacion",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=40,required=True, label="Nombre Completo")
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=50,required=True, label="Apellido(s)")
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	ci = forms.IntegerField(required=True,label="Nro. de CI")
	telefono = forms.IntegerField(required=True,label="Telefono/Celular")
	cargo = forms.ModelChoiceField(queryset=cargo.objects.all())
	def clean_ci(self):
		ci=self.cleaned_data['ci']
		try:
			p=adminstrador.objects.get(ci=ci)
		except adminstrador.DoesNotExist:
			return ci
		raise forms.ValidationError('El Nro. de CI ya Existe')
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","email")
		widgets = {
			'password1':forms.PasswordInput(),
		}
	def save(self,commit=True):
		user=super(UserFormPersonal,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		if commit:
			user.save()
		return user

class CargoForm(ModelForm):
	class Meta:
		model=cargo
		exclude=('estado',)