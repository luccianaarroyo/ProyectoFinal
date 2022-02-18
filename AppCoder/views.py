from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.forms import ConsultaForm
from AppCoder.models import consulta


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def servicios(request):
    return render(request, "AppCoder/servicio.html")

def profesionales(request):
    return render(request, "AppCoder/profesional.html")

def consulta(request):
    return render(request, "AppCoder/consulta.html", 
    {'consulta': consulta.objects.all()})

def consulta_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        nombre = request.POST['nombre']
        servicio = request.POST['servicio']
        mail = request.POST['mail']
        telefono = request.POST['telefono']
        consulta.objects.create(nombre=data['nombre'], servicio=data['servicio'], mail=data['mail'], telefono=data['telefono'])
        return render(request, 'AppCoder/consulta.html')
    
    return render(request, "AppCoder/consultaFormulario.html")