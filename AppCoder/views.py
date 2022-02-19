from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.forms import ConsultaForm
from AppCoder.models import Consulta
from django.template import loader

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def servicios(request):
    return render(request, "AppCoder/servicio.html")

def profesionales(request):
    return render(request, "AppCoder/profesional.html")

def consulta(request):
    return render(request, "AppCoder/consulta.html", {'consulta': Consulta.objects.all()})
    
    

def consulta_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        formulario = ConsultaForm(request.POST) # agrega esto y saca nombre post etc a los 37.15 de la clase 21
        # nombre = request.POST['nombre']
        # servicio = request.POST['servicio']
        # mail = request.POST['mail']
        # telefono = request.POST['telefono'] - modificado por sugerenccia de WP
        if formulario.is_valid():
            data = formulario.cleaned_data
        Consulta.objects.create(nombre =data['nombre'], servicio=data['servicio'], mail=data['mail']) # a los 39.17 de la clase 21 cambia (nombre=nombre, servicio=servicio, mail=mail) 
        return redirect('Consultas')    
    else:
        formulario = ConsultaForm()
    return render(request, "AppCoder/consultaFormulario.html", {'formulario': formulario}) #agrega {formulario} a los 41.20 clase21


#clase 21 a los 1.18 crea esta funcion
def busqueda_consulta(request):
    return render(request, "AppCoder/busquedaConsulta.html")

#clase 21 a los 1.25 crea esta funcion
def buscar(request):
    return HttpResponse(f'Estoy buscando la consulta de: {request.GET["nombre"]}') #el nombre lo saca del template busquedaConsulta en el body esta declarada la variable de busqueda