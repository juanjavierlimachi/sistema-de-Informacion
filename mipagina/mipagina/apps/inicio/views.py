from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from .forms import *#aki estoy importando todos mis formularios de mi achivo form.py
from .models import *##aki estoy importando todos mis models de mi achivo models.py
# Create your views here.
from django.views.generic import TemplateView, FormView,ListView,CreateView
from django.core.urlresolvers import reverse_lazy
import datetime
# Create your views here
#def inicio(request):
	#return render_to_response('inicio/inicio.html',{},context_instance=RequestContext(request))
def Usuario(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado/')
	if request.method=='POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				#si es el super usuario ingresa a privado
				if acceso.is_active and acceso.is_superuser and acceso.is_staff:
					login(request,acceso)
					request.session['session']=[]#creo una session 
					return HttpResponseRedirect('/privado/')
				else:
					if acceso.is_active and acceso.is_staff:
						login(request,acceso)
						return HttpResponseRedirect('/privado/')
					else:
						if acceso.is_active:
							login(request,acceso)
							return HttpResponseRedirect('/privado/')
			else:
				return render_to_response('inicio/nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('inicio/inicio.html',{'formulario':formulario},context_instance=RequestContext(request))


@login_required(login_url='/')
def ingreso(request):
	usuario=request.user
	clave=usuario.id
	est=False
	now = datetime.datetime.now()#Director de la facultad
	if request.user.is_staff and request.user.is_active and request.user.is_superuser:
		try:
			dato=Perfiles.objects.get(usuario_id=clave)
			print "este es mi perfil:",dato
			est=True
		except Perfiles.DoesNotExist:
			pass
		#denuncias=Comment.objects.all().order_by('-id')
		#print request.session.session_key
		return render_to_response('index.html',{'usuario':usuario,'now':now,'est':est},context_instance=RequestContext(request))
	else:
		#Director de Carrera
		a=False
		if request.user.is_active and request.user.is_staff:
			try:
				director=Perfiles.objects.get(usuario_id=clave)
				director=director.carrera
				a=True
				return render_to_response('index.html',{'usuario':usuario,'now':now,'director':director,'a':a},context_instance=RequestContext(request))
			except Perfiles.DoesNotExist:
				director=adminstrador.objects.get(usuario_id=clave)
				director=director.cargo
				print 'este es el valor de A:',a
				return render_to_response('index.html',{'usuario':usuario,'now':now,'director':director,'a':a},context_instance=RequestContext(request))
			else:
				pass
		else:
			if request.user.is_active:
				try:
					director=adminstrador.objects.get(usuario_id=clave)
					#director=director.cargo
					#return render_to_response('index.html',{'usuario':usuario,'now':now,'director':director},context_instance=RequestContext(request))
				except adminstrador.DoesNotExist:
					print 'Tu eres Alumno: ',request.user
					return render_to_response('inicio/Activar.html',{'usuario':usuario,'now':now},context_instance=RequestContext(request))
			else:
				return HttpResponse("Error")

class nuevoUser(FormView):
	#usuario=request.cleaned_data['username']
	#templeta_name es para enviar un atributo form para mi formulariode registro
	template_name = 'inicio/nuevo.html'
	#con form_class indico el formularios estoy utilizando
	#model = User 
	form_class=UserForm
	success_url = reverse_lazy('listaUsuarios')
	def form_valid(self,form):
		user=form.save()
		perfil=Perfiles()
		perfil.usuario = user
		#perfil.nombre=form.cleaned_data['nombre']
		perfil.ci=form.cleaned_data['ci']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.carrera=form.cleaned_data['carrera']
		#perfil.telefono=form.cleaned_data['telefono']
		perfil.save()
		#crear_grupo=Group.objects.get_or_create(name='Cliente')
		#usuario.groups.add(usuario)
		return super(nuevoUser, self).form_valid(form)
def Datos(request,id):
	usuario=User.objects.filter(id=id)
	print usuario
	dato=Perfiles.objects.all(usuario_id=int(id))
	return render_to_response('inicio/datos.html',{'usuario':usuario,'dato':dato},context_instance=RequestContext(request))
 
@login_required(login_url='/')
def serrar(request):
	logout(request)
	return HttpResponseRedirect('/')
@login_required(login_url='/')
def editar_perfil(request):
	if request.method=='POST':
		user_form=UserForms(request.POST,instance=request.user)
		perfil_form=formPerfiles(request.POST,instance=request.user.perfil)
		if user_form.is_valid() and perfil_form.is_valid():
			user_form.save()
			perfil_form.save()
			return HttpResponse("Actualizaste tu perfil correctamente.")
	else:
		user_form=UserForms(instance=request.user)
		perfil_form=formPerfiles(instance=request.user.perfil)
	return render_to_response('inicio/datossss.html',{'user_form':user_form,'perfil_form':perfil_form},context_instance=RequestContext(request))

@login_required(login_url='/')
def editarcontracenia(request):
	id_user=request.user
	if request.method=='POST':
		forms=CambioForm(request.POST)
		if forms.is_valid():
			con=request.POST['Nueva_Contracenia']
			fir=request.POST['Confirmacion']
			if str(con) == str(fir):
				id_user.set_password(con)
				id_user.save()
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Error Los datos no coinsiden")
	else:
		forms=CambioForm()
	return render_to_response('inicio/cambio.html',{'forms':forms},context_instance=RequestContext(request))

	
def index(request):
	return render_to_response('inicio/inicio.html',{},context_instance=RequestContext(request))

@login_required(login_url='/')
def verificacion(request):
	use=request.GET['use']
	try:
		us=User.objects.get(username=use)
		return HttpResponse("El Nombre de Usuario ya exsiste Intente con otro nombre.")
	except User.DoesNotExist:
		return HttpResponse()

@login_required(login_url='/')
def ActivarCuenta(request):
	user=request.user
	use=request.GET['use']
	print "CICICICI",use
	try:
		us=Perfiles.objects.get(ci=use)

		user.is_staff=True
			#user.is_active=True
		user.save()
		if not user.is_active:
			return HttpResponse("Deshabilitado")
		return HttpResponse("bien")
	except Perfiles.DoesNotExist:
		return HttpResponse("Error")

@login_required(login_url='/')
def DasactivarUser(request):
	try:
		nombre=request.GET['nombre']
		staff=request.GET['staff']
		user=User.objects.get(username=nombre)
		if staff=='on':
			user.is_staff=False
			user.is_active=False
			user.save()
			return HttpResponse("El Usuario a sido Deshabilitado")
		else:
			return HttpResponse("Haga click en la casilla para Desactivar esta cuenta")
	except User.DoesNotExist:
		return HttpResponse("Haga click en la casilla para Desactivar esta cuenta")

def VolverHavilitar(request):
	try:
		nombre=request.GET['nombre']
		user=User.objects.get(username=nombre)
		print user.id
		if request.GET['op']== 'ins':
			user.is_staff=False
			user.is_active=True
			user.is_superuser=False
			user.save()
			return HttpResponse("El Usuario a sido Habilitado como Secretaria(a).")
		if request.GET['op']== 'sp':
			user.is_staff=True
			user.is_active=True
			user.is_superuser=False
			user.save()
			return HttpResponse("El Usuario a sido Habilitado como Resp. de Laboratorio")
		else:
			return HttpResponse("Haga click en la casilla para Habilitado esta cuenta")
	except User.DoesNotExist:
		return HttpResponse("Haga click en la casilla para Habilitado esta cuenta")

def DatosUsuario(request):
	users=User.objects.all().order_by("-id")
	perfil=Perfiles.objects.all().order_by("-id")
	t_user=Perfiles.objects.all().count()
	return render_to_response("inicio/DatosUsuario.html",{'users':users,'perfil':perfil,'t_user':t_user},context_instance=RequestContext(request))

def UsuarioVer(request, id):
	user=User.objects.get(id=int(id))
	return render_to_response('inicio/UsuarioVer.html',{'user':user},context_instance=RequestContext(request))



def loginAndroid(request):

	usuario=request.POST['username']
	clave=request.POST['password']
	print "El ususer: ",usuario
	print "La clave",clave
	acceso=authenticate(username=usuario,password=clave)
	if acceso is not None:
		#si es el super usuario ingresa a privado
		if acceso.is_active and acceso.is_superuser and acceso.is_staff:
			login(request,acceso)
			request.session['session']=[]#creo una session
			dic={'username':usuario}
			return HttpResponse(dic)
	else:
		return HttpResponse("Error");
	
#sub sistema Director
class NewPersonal(FormView):
	#usuario=request.cleaned_data['username']
	#templeta_name es para enviar un atributo form para mi formulariode registro
	template_name = 'inicio/nuevoPersonal.html'
	#con form_class indico el formularios estoy utilizando
	#model = User 
	form_class=UserFormPersonal
	success_url = reverse_lazy('listaPersonal')
	def form_valid(self,form):
		usuario=self.request.user
		print "actualllllll",usuario
		clave=usuario.id
		user=form.save()
		perfil=adminstrador()
		perfil.usuario = user
		#perfil.nombre=form.cleaned_data['nombre']
		perfil.ci=form.cleaned_data['ci']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.cargo=form.cleaned_data['cargo']

		director=Perfiles.objects.get(usuario_id=clave)
		director=director.carrera
		car=carrera.objects.get(carrera=director)
		perfil.carrera_id=int(car.id)

		perfil.save()
		#crear_grupo=Group.objects.get_or_create(name='Cliente')
		#usuario.groups.add(usuario)
		return super(NewPersonal, self).form_valid(form)

def listaPersonal(request):
	users=User.objects.all().order_by("-id")
	perfil=adminstrador.objects.all().order_by("-id")
	t_user=adminstrador.objects.all().count()
	return render_to_response("inicio/listaPersonal.html",{'users':users,'perfil':perfil,'t_user':t_user},context_instance=RequestContext(request))

def NewCargo(request):
	if request.method=='POST':
		forms=CargoForm(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
		else:
			return HttpResponse("Error Los datos no coinsiden")
	else:
		forms=CargoForm()
	return render_to_response('inicio/NewCargo.html',{'forms':forms},context_instance=RequestContext(request))
def VerCargo(request):
	cargos=cargo.objects.all().order_by('-id')
	cont=cargo.objects.all().count()
	dic={
		'cargos':cargos,
		'cont':cont
	}
	return render(request,'inicio/VerCargo.html',dic,context_instance=RequestContext(request))

