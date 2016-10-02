#encoding:utf-8
from django.shortcuts import render,render_to_response
from mipagina.apps.carrera.models import *
from mipagina.apps.inicio.models import *
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
# Create your views here.
def NewCarrera(request):
	if request.method=='POST':
		forms=CarreraForm(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
		else:
			return HttpResponse("Error Los datos no coinsiden")
	else:
		forms=CarreraForm()
	return render_to_response('carrera/NewCarrera.html',{'forms':forms},context_instance=RequestContext(request))
def VerCarrera(request):
	carreras=carrera.objects.all().order_by('-id')
	cont=carrera.objects.filter(estado=0).count()
	con=carrera.objects.filter(estado=1).count
	dic={
		'carreras':carreras,
		'cont':cont,
		'con':con
	}
	return render(request,'carrera/VerCarrera.html',dic,context_instance=RequestContext(request))


def NewNoticia(request):
	Usuario=Noticia(usuario=request.user)
	if request.user.is_superuser:
		if request.method=='POST':
			forms=NoticiaForm(request.POST,request.FILES,instance=Usuario)
			if forms.is_valid():
				forms.save()
				return HttpResponse("ok")
			else:
				return HttpResponse("Error Los datos no coinsiden")
		else:
			forms=NoticiaForm()
	else:
		usuario=request.user
		d=Perfiles.objects.get(usuario_id=usuario.id)
		car=carrera.objects.get(carrera=d.carrera)
		print car.id
		if request.method=='POST':
			print request.method
			forms=NoticiaFormDir(request.POST,request.FILES)
			
			noti=Noticia()
			noti.titulo=request.POST['titulo']
			noti.texto=request.POST['texto']
			noti.archivo=request.FILES['archivo']
			noti.carrera_id=car.id
			noti.categoria_id=request.POST['categoria']
			noti.usuario_id=usuario.id
			noti.save()
			return HttpResponse("ok")
		else:
			forms=NoticiaFormDir()
	return render_to_response('carrera/newNoticia.html',{'forms':forms},context_instance=RequestContext(request))

def NewCategoria(request):
	if request.method=='POST':
		forms=CategoriaForm(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
		else:
			return HttpResponse("Error Los datos no coinsiden")
	else:
		forms=CategoriaForm()
	return render_to_response('carrera/newCategoria.html',{'forms':forms},context_instance=RequestContext(request))
def VerCategoria(request):
	categorias=categoria.objects.all().order_by('-id')
	cont=categoria.objects.filter(estado=0).count()
	con=categoria.objects.filter(estado=1).count()
	dic={
		'categorias':categorias,
		'cont':cont,
		'con':con
	}
	return render(request, 'carrera/VerCategoria.html', dic)

def VerNoticia(request):
	noticias=Noticia.objects.all().order_by('-id')
	cont=Noticia.objects.filter(estado=0).count()
	con=Noticia.objects.filter(estado=1).count()
	dic={
		'noticias':noticias,
		'cont':cont,
		'con':con
	}
	return render(request, 'carrera/VerNoticia.html',dic, context_instance=RequestContext(request))
def NewMencion(request):
	if request.method=='POST':
		forms=MencionForm(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
		else:
			return HttpResponse("Error Los datos no coinsiden")
	else:
		forms=MencionForm()
	return render(request, 'carrera/NewMencion.html',{'forms':forms}, context_instance=RequestContext(request))
def VerMenciones(request):
	mensiones=mension.objects.all().order_by('-id')
	cont=mension.objects.filter(estado=0).count()
	con=mension.objects.filter(estado=1).count()
	dic={
		'mensiones':mensiones,
		'cont':cont,
		'con':con
	}
	return render(request,'carrera/VerMenciones.html',dic)

def editCarr(request, id):
	cod=int(id)
	dato=carrera.objects.get(id=int(id))
	print dato
	if request.method=='POST':
		forms=CarreraForm(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El registro se Actualizo correctamente.")
	else:
		forms=CarreraForm(instance=dato)
	return render_to_response('carrera/editCarr.html',{'forms':forms,'cod':cod}, context_instance=RequestContext(request))


def deleteCar(request, id):
	dato=carrera.objects.get(id=int(id))
	return render_to_response('carrera/deleteCar.html',{'dato':dato},context_instance=RequestContext(request))
def deleteCarrera(request, id):
	carrera.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")

def editMension(request, id):
	cod=int(id)
	dato=mension.objects.get(id=int(id))
	print dato
	if request.method=='POST':
		forms=MencionForm(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El registro se Actualizó correctamente.")
	else:
		forms=MencionForm(instance=dato)
	return render_to_response('carrera/editMension.html',{'forms':forms,'cod':cod}, context_instance=RequestContext(request))
def deleteMension(request, id):
	dato=mension.objects.get(id=int(id))
	return render_to_response('carrera/deleteMension.html',{'dato':dato},context_instance=RequestContext(request))
def deleteCarrera(request, id):
	mension.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")

def editNoticia(request, id):
	cod=int(id)
	dato=Noticia.objects.get(id=int(id))
	#Usuario=Noticia(usuario=request.user)
	if request.user.is_superuser:
		if request.method=='POST':
			forms=NoticiaForm(request.POST,request.FILES,instance=dato)
			if forms.is_valid():
				forms.save()
				return HttpResponse("El registro se Actualizó correctamente.")
			else:
				return HttpResponse("Error Los datos no coinsiden")
		else:
			forms=NoticiaForm(instance=dato)
	else:
		usuario=request.user
		d=Perfiles.objects.get(usuario_id=usuario.id)
		car=carrera.objects.get(carrera=d.carrera)
		print car.id
		if request.method=='POST':
			forms=NoticiaFormDir(request.POST,request.FILES,instance=dato)
			if forms.is_valid():
				forms.save()
				return HttpResponse("El registro se Actualizó correctamente.")
			else:
				return HttpResponse("Error Los datos no coinsiden")
		else:
			forms=NoticiaFormDir(instance=dato)
	return render_to_response('carrera/editNoticia.html',{'forms':forms,'cod':cod}, context_instance=RequestContext(request))

def deleteNoticia(request, id):
	dato=Noticia.objects.get(id=int(id))
	return render_to_response('carrera/deleteNoticia.html',{'dato':dato},context_instance=RequestContext(request))
def DeleteNoticias(request, id):
	Noticia.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")
def editCateg(request, id):
	cod=int(id)
	dato=categoria.objects.get(id=int(id))
	print dato
	if request.method=='POST':
		forms=CategoriaForm(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El registro se Actualizó correctamente.")
	else:
		forms=CategoriaForm(instance=dato)
	return render_to_response('carrera/editCateg.html',{'forms':forms,'cod':cod}, context_instance=RequestContext(request))

def deleteCate(request, id):
	dato=categoria.objects.get(id=int(id))
	return render_to_response('carrera/deleteCate.html',{'dato':dato},context_instance=RequestContext(request))
def DeleteCategorias(request, id):
	categoria.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")



