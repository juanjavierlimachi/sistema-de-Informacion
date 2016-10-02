from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
urlpatterns = patterns('',
	#sub sistema facultad
    url(r'^$', Usuario),
	url(r'^privado/$', ingreso),
	url(r'^cerrar/$', serrar),
	url(r'^datos/(?P<id>\d+)/$',Datos),#de Prueva
	url(r'^editarperfil/$',editar_perfil),
	url(r'^nuevo/$',nuevoUser.as_view(), name='nuevoUser'),
	url(r'^ActivarCuenta/$',ActivarCuenta),
	url(r'^editarcontracenia/$', editarcontracenia),
	url(r'^verificacion/$',verificacion, name='verificacion'),
	url(r'^DatosUsuario/$', DatosUsuario, name='listaUsuarios'),
	url(r'^UsuarioVer/(?P<id>\d+)/$',UsuarioVer),
	url(r'^DasactivarUser/$',DasactivarUser),
	url(r'^VolverHavilitar/$',VolverHavilitar),

	url(r'^loginAndroid/$',loginAndroid),

	#sub sistema director
	
	url(r'^NewPersonal/$',NewPersonal.as_view(), name='NewPersonal'),
	url(r'^listaPersonal/$', listaPersonal, name='listaPersonal'),
	url(r'^NewCargo/$',NewCargo),
	url(r'^VerCargo/$',VerCargo),
	

)
