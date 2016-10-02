from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
urlpatterns = patterns('',

	url(r'^NewCarrera/$',NewCarrera),
	url(r'^VerCarrera/$',VerCarrera),

	url(r'^NewNoticia/$',NewNoticia),
	url(r'^NewCategoria/$',NewCategoria),
	url(r'^VerCategoria/$',VerCategoria),
	url(r'^VerNoticia/$',VerNoticia),
	url(r'^NewMencion/$',NewMencion),
	url(r'^VerMenciones/$',VerMenciones),

	
	url(r'^EditCarr/(?P<id>\d+)/$',editCarr),
	
	url(r'^deleteCar/(?P<id>\d+)/$',deleteCar),
	url(r'^deleteCarrera/(?P<id>\d+)/$',deleteCarrera),

	
	url(r'^EditMension/(?P<id>\d+)/$',editMension),
	url(r'^deleteMensio/(?P<id>\d+)/$',deleteMension),
	url(r'^DeleteCarrera/(?P<id>\d+)/$',deleteCarrera),

	url(r'^EditNoticia/(?P<id>\d+)/$',editNoticia),
	url(r'^deleteNoticia/(?P<id>\d+)/$',deleteNoticia),
	url(r'^DeleteNoticias/(?P<id>\d+)/$',DeleteNoticias),

	url(r'^editCate/(?P<id>\d+)/$',editCateg),
	url(r'^deleteCate/(?P<id>\d+)/$',deleteCate),
	url(r'^DeleteCategorias/(?P<id>\d+)/$',DeleteCategorias),

)