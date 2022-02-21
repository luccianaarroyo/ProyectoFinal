from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from TrabajoFinal.forms import UserRegisterForm


def login_request (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return redirect ('inicio/')
            else:
                return render(request, 'login.htlm',
                              {'form': form,
                               'error': 'No es valido el usuario y contraseña'})

        else:
            return redirect('inicio')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    
def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} creado correctamente')
    else:
        form = UserRegisterForm()
        
    return render(request,'registro.html', {'form': form})