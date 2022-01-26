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
    return render(request, "AppCoder/consulta.html")

def consulta_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        formulario = ConsultaForm(request.POST)
       
        if formulario.is_valid():
            data = formulario.cleaned_data
            consulta.objects.create(nombre=data['nombre'], servicio=data['servicio'], mail=data['mail'], telefono=data['telefono']) #curso = curso de forms.py
            return redirect('Consulta')
    else:
        formulario = ConsultaForm()
    return render(request, 'AppCoder/ConsultaFormulario.html', {'formulario': formulario})