from django.shortcuts import render
from django.http import HttpResponse

def sucursal(request):
    return render(request, "AppCoder/sucursal.html")

def servicio(request):
    return render(request, "AppCoder/servicio.html")

def profesional(request):
    return render(request, "AppCoder/profesional.html")

def turno(request):
    return render(request, "AppCoder/turno.html")

def cliente(request):
    return render(request, "AppCoder/cliente.html")