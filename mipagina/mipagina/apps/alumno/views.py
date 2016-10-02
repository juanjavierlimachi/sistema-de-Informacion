#encoding:utf-8
from django.shortcuts import render,render_to_response
from .models import *
from .forms import *
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime, date, time, timedelta
import calendar
# Create your views here.
def verDefensas(request):
	tribunales=tesis.objects.all().order_by('-id')
	cont=tesis.objects.filter(estado=0).count()
	con=tesis.objects.filter(estado=1).count()
	carreras=carrera.objects.filter(estado=0)
	dic={
		'tribunales':tribunales,
		'cont':cont,
		'con':con,
		'carreras':carreras
	}
	return render(request,'alumno/VerDefensas.html',dic,context_instance=RequestContext(request))
import time
def NewDefensa(request):
	if request.method=='POST':
		forms=TesisForm(request.POST)
		if forms.is_valid():
			#forms.save()
			defensa=tesis()
			defensa.titulo=request.POST['titulo']
			defensa.modaliad=request.POST['modaliad']
			defensa.alumno_id=int(request.POST['alumno'])
			defensa.numero_documento=request.POST['numero_documento']
			#2016-09-09
			defensa.fecha_de_defensa=datetime.strptime(request.POST['fecha_de_defensa'],"%Y-%m-%d").date()
			defensa.hora_de_la_defensa=time.strftime(request.POST['hora_de_la_defensa'])
			defensa.lugar=request.POST['lugar']
			defensa.save()

			#codDef=tesis.objects.latest('id')
			print "Defensa:::::",defensa.id
			cod=defensa.id
			return HttpResponse(cod)

	else:
		forms=TesisForm()
	return render(request,'alumno/NewDefensa.html',{'forms':forms},context_instance=RequestContext(request))

def NewDefensaAlumno(request, id):
	alum=int(id)
	codDef=Alumno.objects.get(id=int(id))
	#tema=request.session['session']
	tema=''
	for i in request.session['session']:
		tema=i
	print "esta session:",tema
	if request.method=='POST':
		forms=TesisForm(request.POST)
		if forms.is_valid():
			#forms.save()
			defensa=tesis()
			defensa.titulo=request.POST['titulo']
			defensa.modaliad=tema
			defensa.alumno_id=alum
			defensa.numero_documento=request.POST['numero_documento']
			#2016-09-09
			defensa.fecha_de_defensa=datetime.strptime(request.POST['fecha_de_defensa'],"%Y-%m-%d").date()
			defensa.hora_de_la_defensa=time.strftime(request.POST['hora_de_la_defensa'])
			defensa.lugar=request.POST['lugar']
			defensa.save()

			#codDef=tesis.objects.latest('id')
			print "Defensa:::::",defensa.id
			cod=defensa.id
			return HttpResponse(cod)
	else:
		forms=TesisForm()
	return render(request,'alumno/DefensaAluno.html',{'codDef':codDef,'forms':forms,'tema':tema},context_instance=RequestContext(request))


def newTribunal(request):
	if request.method=='POST':
		forms=TribunalForm(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=TribunalForm()
	return render(request,'alumno/newTribunal.html',{'forms':forms},context_instance=RequestContext(request))
def vertribunales(request):
	tribunales=Tribunal.objects.all().order_by('-id')
	cont=Tribunal.objects.filter(estado=0).count()
	con=Tribunal.objects.filter(estado=1).count()
	dic={
		'tribunales':tribunales,
		'cont':cont,
		'con':con
	}
	return render(request,'alumno/vertribunales.html',dic,context_instance=RequestContext(request))

def datalleDefensa(request, id):
	dato=tesis.objects.get(id=int(id))
		#print "Los trinunales",dato.tribunal
	id_alumno=Alumno.objects.get(id=int(dato.alumno.id))
	hora=False
	if dato.calificacion != None:
		hora=True
	return render(request, 'alumno/datalleDefensa.html',{'dato':dato,'hora':hora,'id_alumno':id_alumno},context_instance=RequestContext(request))

def Agergartri(request, id):
	cod=id
	if request.method=='POST':
		forms=TribunalFormAdd(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=TribunalFormAdd()
	return render(request,'alumno/Agergartri.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def buscarTrinunal(request):
	
	if request.method=="POST":
		texto = request.POST['uno']
		busqueda=(
				Q(nombre__icontains=texto) |
				Q(apellido_paterno__icontains=texto) |
				Q(apellido_materno__icontains=texto)
			)
		resultados=Tribunal.objects.filter(busqueda).distinct()
		print "coinsidencias",resultados
		return render_to_response('alumno/buscarTrinunal.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET['uno']
		print texto
		busqueda=(
				Q(nombre__icontains=texto) |
				Q(apellido_paterno__icontains=texto) |
				Q(apellido_materno__icontains=texto)
			)
		resultados=Tribunal.objects.filter(busqueda).distinct()
		return render_to_response('alumno/buscarTrinunal.html',{'resultados':resultados},context_instance=RequestContext(request))
def AddTribunal(request):
	datos=int(request.POST['tribunal_1'])#este es el dato del tribunal
	dato2=int(request.POST['tribunal_2'])
	dato3=int(request.POST['tribunal_3'])
	print "el tribunal:",datos
	tt=request.POST['cod']
	print "Latasis: ",tt
	te=tesis.objects.get(id=int(tt))
	te.tribunal.add(datos,dato2,dato3)#agrego el tribunal que busque
	print tt
	tesis.objects.filter(id=int(tt)).update(hora_de_Conclucion=request.POST['hora'],calificacion=request.POST['calificacion'])
	return HttpResponse(datos)
def buscarTrinunalDos(request):
	texto=request.GET['dos']
	print texto
	busqueda=(
			Q(nombre__icontains=texto) |
			Q(apellido_paterno__icontains=texto) |
			Q(apellido_materno__icontains=texto)
		)
	resultados=Tribunal.objects.filter(busqueda).distinct()
	return render_to_response('alumno/buscarTrinunalDos.html',{'resultados':resultados},context_instance=RequestContext(request))

def buscarTrinunalTres(request):
	texto=request.GET['tres']
	print texto
	busqueda=(
			Q(nombre__icontains=texto) |
			Q(apellido_paterno__icontains=texto) |
			Q(apellido_materno__icontains=texto)
		)
	resultados=Tribunal.objects.filter(busqueda).distinct()
	return render_to_response('alumno/buscarTrinunalTres.html',{'resultados':resultados},context_instance=RequestContext(request))
import locale
def resolucion(request, id):
	fecha=datetime.now()
	dato=tesis.objects.get(id=int(id))
	id_alumno=Alumno.objects.get(id=int(dato.alumno.id))
	#print "Defensa::::",dato.fecha_de_defensa.day
	di="%A"
	#print dato.fecha_de_defensa.strftime(di)
	dia= dato.fecha_de_defensa.strftime(di)
	m="%B"
	#mes=dato.fecha_de_defensa.strftime("%B")
	ahora=datetime.now()
	fech=datetime.today()
	mes=fech.strftime("%B")
	anio=fech.strftime("%Y")
	horas=dato.hora_de_la_defensa.strftime("%H:%M")
	dias = ['','un','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trese','catorce','quince','dieciséis','diecisiete','dieciocho','diecinueve','veinte','veinte y uno','veinte y dos','veinte y tres','veinte y cuatro','veinte y cinco','veinte y seis','veinte y siete','veinte y ocho','veinte y nueve','treinta','treinta y uno']
	dd = dias[ahora.day]
	if anio=='2016':
		anio=dias[16]
		print "aaaa",anio
	elif anio == '2017':
		anio=dias[17]
		print "aaaa",anio
	dic={
		'dato':dato,
		'id_alumno':id_alumno,
		'fecha':fecha,
		'dia':dia,
		'dias':dd,
		'mes':mes,
		'anio':anio,
		'horas':horas
	}
	return render(request,'alumno/resolucion1.html',dic,context_instance=RequestContext(request))

def citacion(request, id):
	fecha=date.today()
	dato=tesis.objects.get(id=int(id))
	id_alumno=Alumno.objects.get(id=int(dato.alumno.id))
	horas=dato.hora_de_la_defensa.strftime("%H:%M")
	dic={
		'dato':dato,
		'id_alumno':id_alumno,
		'fecha':fecha,
		'horas':horas
	}
	return render(request,'alumno/citacion.html',dic,context_instance=RequestContext(request))
def examen(request, id):
	fecha=datetime.today()
	dato=tesis.objects.get(id=int(id))
	id_alumno=Alumno.objects.get(id=int(dato.alumno.id))

	dic={
		'dato':dato,
		'id_alumno':id_alumno,
		'fecha':fecha
	}
	return render(request,'alumno/examen.html',dic,context_instance=RequestContext(request))
def publicacion(request, id):
	fecha=datetime.today()
	dato=tesis.objects.get(id=int(id))
	id_alumno=Alumno.objects.get(id=int(dato.alumno.id))

	dic={
		'dato':dato,
		'id_alumno':id_alumno,
		'fecha':fecha
	}
	return render(request,'alumno/publicacion.html',dic,context_instance=RequestContext(request))
def solicitud(request, id):
	fecha=datetime.today()
	dato=tesis.objects.get(id=int(id))
	id_alumno=Alumno.objects.get(id=int(dato.alumno.id))

	dic={
		'dato':dato,
		'id_alumno':id_alumno,
		'fecha':fecha
	}
	return render(request,'alumno/solicitud.html',dic,context_instance=RequestContext(request))
def newAlumno(request):
	carreras=carrera.objects.filter(estado=0).order_by("-id")
	request.session['session']=[]
	Usuario=Alumno(usuario=request.user)
	if request.method=='POST':

		forms=AlumnoForm(request.POST,instance=Usuario)
		formsTesis=formulariotesis(request.POST)
		if forms.is_valid() and formsTesis.is_valid():
			
			alumno=Alumno()
			alumno.nombre=request.POST['nombre']
			alumno.apellido_paterno=request.POST['apellido_paterno']
			alumno.apellido_materno=request.POST['apellido_materno']
			alumno.sexo=request.POST['sexo']
			alumno.ci=request.POST['ci']
			alumno.departamento=request.POST['departamento']

			alumno.carrera_id=int(request.POST['car'])
			alumno.usuario_id=int(request.user.id)
			alumno.save()#Guardo los datos del alumno
			#forms.save()
			defensa=tesis()
			defensa.titulo=request.POST['titulo']
			defensa.mension_id=int(request.POST['men'])
			defensa.modaliad=request.POST['ttt']
			defensa.alumno_id=alumno.id
			defensa.carrera_id=int(request.POST['car'])
			defensa.numero_documento=request.POST['numero_documento']
			#2016-09-09
			defensa.fecha_de_defensa=datetime.strptime(request.POST['fecha_de_defensa'],"%Y-%m-%d").date()
			defensa.hora_de_la_defensa=time.strftime(request.POST['hora_de_la_defensa'])
			defensa.lugar=request.POST['lugar']
			defensa.save()

			#codDef=tesis.objects.latest('id')
			cod = alumno.id
			
			return HttpResponse(cod)
			#return render(request,'alumno/DefensaAluno.html/',{'codDef':codDef}, context_instance=RequestContext(request))
	else:
		forms=AlumnoForm()
		formsTesis=formulariotesis()
	return render(request,'alumno/newAlumno.html',{'forms':forms,'formsTesis':formsTesis,'carreras':carreras},context_instance=RequestContext(request))

#def optenerTema(request):
	#forms=formTema()
	#return render(request, 'alumno/optenerTema.html',{'forms':forms},context_instance=RequestContext(request))
def verAlumnos(request):
	alumnos=Alumno.objects.all().order_by('-id')
	cont=Alumno.objects.filter(estado=0).count()
	con=Alumno.objects.filter(estado=1).count()
	carreras=carrera.objects.filter(estado=0)
	dic={
		'alumnos':alumnos,
		'cont':cont,
		'con':con,
		'carreras':carreras
	}
	return render(request,'alumno/VerAlumnos.html',dic,context_instance=RequestContext(request))
def Editalumno(request, id):
	cod=int(id)
	dato=Alumno.objects.get(id=int(id))
	print dato
	if request.method=='POST':
		forms=AlumnoForm(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El registro se Actualizo correctamente.")
	else:
		forms=AlumnoForm(instance=dato)
	return render_to_response('alumno/Editalumno.html',{'forms':forms,'cod':cod}, context_instance=RequestContext(request))
def deleteAlumno(request, id):
	dato=Alumno.objects.get(id=int(id))
	return render_to_response('alumno/deleteAlumno.html',{'dato':dato},context_instance=RequestContext(request))
def delAlumno(request, id):
	Alumno.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")

def buscarAlumno(request):
	texto=request.GET['nombre']
	print texto
	busqueda=(
			Q(nombre__icontains=texto) |
			Q(apellido_paterno__icontains=texto) |
			Q(apellido_materno__icontains=texto)
		)
	resultados=Alumno.objects.filter(busqueda).distinct()
	return render_to_response('alumno/buscarAlumno.html',{'resultados':resultados},context_instance=RequestContext(request))
def PerfilAlumno(request, id):
	tiene=False
	dato=Alumno.objects.get(id=int(id))
	try:
		defensa=tesis.objects.get(alumno_id=int(dato.id))
		tiene=True
		defe=defensa
		dic={'dato':dato,'tiene':tiene,'defe':defe}
		return render(request,'alumno/PerfilAlumno.html',dic,context_instance=RequestContext(request))
	except tesis.DoesNotExist:
		#return HttpResponse("EEEE")
		dic={'dato':dato,'tiene':tiene}
		return render(request,'alumno/PerfilAlumno.html',dic,context_instance=RequestContext(request))
def AgregarHora(request, id):
	cod=int(id)
	tema=tesis.objects.get(id=int(id))
	if request.method=='POST':
		tesis.objects.filter(id=int(id)).update(hora_de_Conclucion=request.POST['hora'],calificacion=request.POST['calificacion'])
		print "Teee",tema.id
		return HttpResponse(tema.id)

	return render(request,'alumno/AgregarHora.html',{'cod':cod},context_instance=RequestContext(request))
def editTribunal(request, id):
	cod=int(id)
	dato=Tribunal.objects.get(id=int(id))
	print dato
	if request.method=='POST':
		forms=TribunalForm(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El registro se Actualizo correctamente.")
	else:
		forms=TribunalForm(instance=dato)
	return render_to_response('alumno/editTribunal.html',{'forms':forms,'cod':cod}, context_instance=RequestContext(request))
def deletetribunal(request, id):
	dato=Tribunal.objects.get(id=int(id))
	return render_to_response('alumno/deletetribunal.html',{'dato':dato},context_instance=RequestContext(request))
def deltribunal(request, id):
	Tribunal.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")

def buscar(request):
    if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
        texto=request.POST["q"]
        busqueda=(
            Q(nombre__icontains=texto) |
            Q(apellido_paterno__icontains=texto) |
            Q(apellido_materno__icontains=texto)
        )
        resultados=Tribunal.objects.filter(busqueda).distinct()
        print "Clente:",resultados
        return render_to_response('alumno/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

    else:
        texto=request.GET["q"]
        busqueda=(
            Q(nombre__icontains=texto) |
            Q(apellido_paterno__icontains=texto) |
            Q(apellido_paterno__icontains=texto)
        )
        resultados=Tribunal.objects.filter(busqueda).distinct()
        # html="<ul class='ul_lista'>"
        # for i in resultados:
        #     html=html+"<li><a href='/detalles/"+str(i.id)+"/'>"+i.Nombre_trabajador+""+i.Apellidos+"</a></li>"
        # html=html+"<ul>"
        return render_to_response('alumno/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))
def escogido(request, id):
	dato=Tribunal.objects.get(id=int(id))
	dic={
		'dato':dato
	}
	return render(request,'alumno/escogido.html',dic,context_instance=RequestContext(request))

def DefensaTribunal(request, id):
	datos=tesis.objects.filter(tribunal=int(id))
	print datos
	dic={
		'datos':datos
	}
	return render(request,'alumno/DefensaTribunal.html',dic,context_instance=RequestContext(request))
def por_carreras(request, id):
	datos=Alumno.objects.filter(carrera_id=int(id))
	cont=Alumno.objects.filter(carrera_id=int(id), estado=0).count()
	con= Alumno.objects.filter(carrera_id=int(id), estado=1).count()
	dic={
		'alumnos':datos,
		'cont':cont,
		'con':con
	}
	return render(request, 'alumno/por_carreras.html',dic,context_instance=RequestContext(request))
def defesas_por_carreras(request, id):
	datos=tesis.objects.filter(carrera_id=int(id)).order_by("-id")
	cont=Alumno.objects.filter(carrera_id=int(id), estado=0).count()
	con= Alumno.objects.filter(carrera_id=int(id), estado=1).count()
	dic={
		'datos':datos,
		'cont':cont,
		'con':con
	}
	#select * from defensa d, alumno a where int=.a.carrera and 
	return render(request, 'alumno/defesas_por_carreras.html',dic,context_instance=RequestContext(request))
def consultar(request):
	dato=carrera.objects.get(id=int(request.GET['carrera']))
	print "Carrera",dato

	return HttpResponse(dato.carrera)
def consultarInfo(request):
	dato=carrera.objects.get(id=int(request.GET['carrera']))
	print "Carrera",dato
	html=''
	if dato.carrera == 'Contrucciones Civiles':
		html="<ul class='ul_lista'><li>1.- construcciones</li></ul>"

	if dato.carrera == 'Ingenieria Civil':
		html="<ul class='ul_lista'><li><input name='salida' id='salida' type='checkbox' />  1 .- Archivador Valorado Universitario</li><li><input name='salida' id='salida' type='checkbox' /> 2.- Memorial dirigido el señor Decano, solicitando señalamiento de dia hora para el examen</li><li><input name='salida' id='salida' type='checkbox' /> 3.- Certificado de revicion de Ortografia, Sintaxis etc. otorgado por un profesor de literatura</li><li><input name='salida' id='salida' type='checkbox' /> 4.- Boleta aporte de Bs 365.00 (Tesis en Limpio)</li><li><input name='salida' id='salida' type='checkbox' /> 5.- Certificado de cumplimineto del trabajo en la institucion otorgado por la institución<li><input name='salida' id='salida' type='checkbox' /> 6.- Boleta aporte de $ 50.00 'fondo pro-libro', Biblioteca carrera</li><li><input name='salida' id='salida' type='checkbox' /> 7.- Boleta de pago por servicio de empaste en extención Universitaria (fotocopia)</li><li><input name='salida' id='salida' type='checkbox' /> 8.- Solvencia Univercitaria Actualizada, Original</li><li><input name='salida' id='salida' type='checkbox' /> 9.- Boleta de Matricula y programación de CIV-400 Originales.</li><li><input name='salida' id='salida' type='checkbox' /> 10.- Boleta Matricula y programacion original</li><li><input name='salida' id='salida' type='checkbox' /> 10.- Una hoja de papel sellado Universitario con timbres de Bs. 3.50</li><li><input name='salida' id='salida' type='checkbox' /> 11.- Una hoja de papel sellado Universitario con timbres de Bs. 3.50</li><li><input name='salida' id='salida' type='checkbox' /> 12.- Trabajo en limpio (anillado), 3 ejemplares (si contiene planos deben ser fijados en el enpaste)</li><li><input name='salida' id='salida' type='checkbox' /> 13.- Medio magnetico 2 CDs (en soble flexible), para Biblioteca Virtual D.S.A.</li><li>Tramites de Titulos Planta Baja Edificio Administrativo</li></ul>"

	if dato.carrera == 'Ingenieria  de Sistemas':
		html="<ul class='ul_lista'><li><input name='salida' id='salida' type='checkbox' /> 1 .- Archivador Valorado Universitario</li><li><input name='salida' id='salida' type='checkbox' /> 2.- Memorial dirigido el señor Decano, solicitando señalamiento de dia hora para el examen</li><li><input name='salida' id='salida' type='checkbox' /> 3.- Defensa Oral, en papel sellado universitario con timbres de Bs 21</li><li><input name='salida' id='salida' type='checkbox' /> 4.- Certificado de revicion de Ortografia, Sintaxis etc. otorgado por un profesor de literatura</li><li><input name='salida' id='salida' type='checkbox' /> 5.- Certificado de cumplimineto del trabajo en la instatucion con que se suscribio el convenio</li><li><input name='salida' id='salida' type='checkbox' /> 6.- Informe tecnico sobre el trabajo desarrollado en la institucion correspondiente</li><li><input name='salida' id='salida' type='checkbox' /> 7.- boleta aporte de $ 50.00 (Defensa de Tesis)</li><li><input name='salida' id='salida' type='checkbox' /> 8.- boleta aporte de $ 50.00 'fondo pro-libro', biblioteca carrera Ingenieria de sistemas</li><li><input name='salida' id='salida' type='checkbox' /> 9.- Solvencia Univercitaria Actualizada, Original</li><li><input name='salida' id='salida' type='checkbox' /> 10.- Una hoja de papel sellado Universitario con timbres de Bs. 3.50</li><li><input name='salida' id='salida' type='checkbox' /> 11.- boleta Matricula y programacion original</li><li><input name='salida' id='salida' type='checkbox' /> 12.- Trabajo en linpio (anillado), 3 ejemplares (si contiene planos deben ser fijados en el enpaste)</li><li><input name='salida' id='salida' type='checkbox' /> 13.- Medio magnetico 2 CDs (en soble flexible), para Biblioteca Virtual D.S.A.</li><li>Tramites de Titulos Planta Baja Edificio Administrativo</li></ul>"

	if dato.carrera == 'Geodecia y Topografia':
		html="<ul class='ul_lista'><li><input name='salida' id='salida' type='checkbox' /> 1 .- Archivador Valorado Universitario</li><li><input name='salida' id='salida' type='checkbox' /> 2.- Memorial dirigido el señor Decano, solicitando señalamiento de dia hora para el examen</li><li><input name='salida' id='salida' type='checkbox' /> 4.- Certificado de revicion de Ortografia, Sintaxis etc. otorgado por un profesor de literatura</li><li><input name='salida' id='salida' type='checkbox' /> 7.- Boleta aporte de Bs 365.00 (Tesis en Limpio)</li><li><input name='salida' id='salida' type='checkbox' /> 8.- boleta aporte de $ 50.00 'fondo pro-libro', biblioteca carrera</li><li><input name='salida' id='salida' type='checkbox' /> Boleta de pago por servicio de empaste en extencion Universitaria (fotocopia)</li><li>9.- Solvencia Universitario Actualizada, Original</li><li><input name='salida' id='salida' type='checkbox' /> 10.- Boleta de Matricula y programacion de GEO-503 Originales.</li><li><input name='salida' id='salida' type='checkbox' /> 11.- boleta Matricula y programacion original</li><li><input name='salida' id='salida' type='checkbox' /> 10.- Una hoja de papel sellado Universitario con timbres de Bs. 3.50</li><li><input name='salida' id='salida' type='checkbox' /> 12.- Trabajo en linpio (anillado), 3 ejemplares (si contiene planos deben ser fijados en el enpaste)</li><li><input name='salida' id='salida' type='checkbox' />13.- Medio magnetico 2 CDs (en soble flexible), para Biblioteca Virtual D.S.A.</li><li><input name='salida' id='salida' type='checkbox' /> Tramites de Titulos Planta Baja Edificio Administrativo</li></ul>"

		return HttpResponse(html)
	return HttpResponse(html)
def buscarAlumnoView(request):
	if request.method=="POST":
		texto = request.POST['p']
		busqueda=(
				Q(nombre__icontains=texto) |
				Q(apellido_paterno__icontains=texto) |
				Q(ci__icontains=texto)
			)
		resultados=Alumno.objects.filter(busqueda).distinct()
		print "coinsidencias",resultados
		return render_to_response('alumno/buscarAlumnoView.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET['p']
		print texto
		busqueda=(
				Q(nombre__icontains=texto) |
				Q(apellido_paterno__icontains=texto) |
				Q(apellido_materno__icontains=texto)
			)
		resultados=Alumno.objects.filter(busqueda).distinct()
		return render_to_response('alumno/buscarAlumnoView.html',{'resultados':resultados},context_instance=RequestContext(request))
def ShearMension(request):
	texto=request.GET['mension']
	print texto
	busqueda=(
			Q(mension__icontains=texto) |
			Q(mension__icontains=texto) |
			Q(mension__icontains=texto)
		)
	resultados=mension.objects.filter(busqueda).distinct()
	return render_to_response('alumno/ShearMension.html',{'resultados':resultados},context_instance=RequestContext(request))
def Updatedefensa(request, id):
	cod=id
	dato=tesis.objects.get(id=int(id))
	if request.method == 'POST':
		forms=Updateformtesis(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse(cod)
	else:
		forms = Updateformtesis(instance=dato)
	return render_to_response('alumno/Updatedefensa.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def DeleteDefensa(request, id):
	dato=tesis.objects.get(id=int(id))
	return render_to_response('alumno/DeleteDefensa.html',{'dato':dato},context_instance=RequestContext(request))
def Deletedefensa(request, id):
	tesis.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó Correctamente.")