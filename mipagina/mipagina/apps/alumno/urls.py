from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
urlpatterns = patterns('',
	#url(r'^privado/$', ingreso),
	url(r'^NewTribunal/$',newTribunal),
	
	url(r'^Vertribunales/$',vertribunales),
	url(r'^NewDefensa/$',NewDefensa),
	
	url(r'^VerDefensas/$',verDefensas),

	url(r'^datalles/(?P<id>\d+)/$',datalleDefensa),
	url(r'^Agergartri/(?P<id>\d+)/$',Agergartri),
	url(r'^buscarTrinunal/$',buscarTrinunal),

	url(r'^addTribunal/$',AddTribunal),
	url(r'^buscarTrinunalDos/$',buscarTrinunalDos),
	url(r'^buscarTrinunalTres/$',buscarTrinunalTres),

	url(r'^resolucion/(?P<id>\d+)/$',resolucion),
	url(r'^citacion/(?P<id>\d+)/$',citacion),
	url(r'^examen/(?P<id>\d+)/$',examen),
	url(r'^publicacion/(?P<id>\d+)/$',publicacion),
	url(r'^solicitud/(?P<id>\d+)/$',solicitud),
	
	url(r'^NewAlumno/$',newAlumno),
	url(r'^VerAlumnos/$',verAlumnos),

	url(r'^Editalumno/(?P<id>\d+)/$',Editalumno),
	url(r'^deleteAlumno/(?P<id>\d+)/$',deleteAlumno),
	url(r'^delAlumno/(?P<id>\d+)/$',delAlumno),
	url(r'^buscarAlumno/$',buscarAlumno),

	url(r'^PerfilAlumno/(?P<id>\d+)/$',PerfilAlumno),

	url(r'^NewDefensaAlumno/(?P<id>\d+)/$',NewDefensaAlumno),
	url(r'^AgregarHora/(?P<id>\d+)/$',AgregarHora),

	url(r'^EditTribunal/(?P<id>\d+)/$',editTribunal),
	
	url(r'^deletetribunal/(?P<id>\d+)/$',deletetribunal),
	url(r'^deltribunal/(?P<id>\d+)/$',deltribunal),
	url(r'^buscar/$',buscar),
	url(r'^escogido/(?P<id>\d+)/$',escogido),
	url(r'^DefensaTribunal/(?P<id>\d+)/$',DefensaTribunal),
	url(r'^por_carreras/(?P<id>\d+)/$',por_carreras),
	url(r'^defesas_por_carreras/(?P<id>\d+)/$',defesas_por_carreras),
	url(r'^consultar/$',consultar),
	url(r'^consultarInfo/$',consultarInfo),
	url(r'^buscarAlumnoView/$',buscarAlumnoView),
	url(r'^ShearMension/$',ShearMension),
	url(r'^Updatedefensa/(?P<id>\d+)/$',Updatedefensa),
	url(r'^DeleteDefensa/(?P<id>\d+)/$',DeleteDefensa),
	url(r'^Deletedefensa/(?P<id>\d+)/$',Deletedefensa),
)
