from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from TrabajoFinal.forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return redirect('inicio/')
            else:
                return render(request, 'login.htlm',
                              {'form': form,
                               'error': 'No es valido el usuario y contraseña'})

        else:
            return redirect('inicio/')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} creado correctamente')
    else:
        form = UserRegisterForm()

    return render(request, 'registro.html', {'form': form})


class UserCreateView(CreateView):
    model= User
    success_url = reverse_lazy('login')
    template_name = 'registro.html'
    form_class = UserRegisterForm
 
@login_required  
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.password = data['password1']
            
            usuario.save()
            return redirect('inicio/')
    else:
        formulario = UserEditForm({'emial' : usuario.email})
        
    return render(request, 'registro.html', {'form' : formulario})