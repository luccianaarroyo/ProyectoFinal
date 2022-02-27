from pyexpat import model
from django.forms import model_to_dict
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.urls import reverse_lazy  

from AppCoder.forms import ServiciosForm, ProfesionalesForm, ConsultaForm, AvatarForm
from AppCoder.models import Servicios, Profesionales, Consulta, Avatar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#AGREGADO VIERNES 18.35
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView

def inicio(request):
    #---- AVATAR ROMPE NO RECONOSE OBJETS ---- 
    avatar = Avatar.objects.filter(user=request.user)

    if avatar:
        avatar_url = avatar.last().imagen.url
    else:
        avatar_url = ''

    return render(request, 'AppCoder/inicio.html', {'avatar_url': avatar_url})
   

############ SERVICIOS ###########

def servicios(request):
    return render(request, "AppCoder/servicio.html", {'profesionales': Servicios.objects.all()})

def servicios_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        formulario = ServiciosForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        Servicios.objects.create(nombre =data['nombre'], servicio=data['servicio'], detalleDeServicio=data['detalleDeServicio']) 
        return redirect('Servicios')    
    else:
        formulario = ServiciosForm()
    return render(request,"AppCoder/consultaFormulario.html", {'formulario': formulario}) 

def servicios_delete (request, id_servi):
    servicios = Servicios.objects.get(id=id_servi)
    servicios.delete()
    
    return redirect('Servicios')

def servicios_update(request, id_servi):
    servicios = Servicios.objects.get(id=id_servi)
    
    if request.method == 'POST':
         formulario = ServiciosForm(request.POST)

         if formulario.is_valid():
             data = formulario.cleaned_data
             servicios.nombre = data ['nombre']
             servicios.servicio = data ['servicio']
             servicios.detalleDeServicio = data ['detalleDeServicio']
            
             servicios.save()
            
             return redirect ('Servicios')
    else:
        formulario = ServiciosForm(model_to_dict(servicios))
    return render(request, 'AppCoder/consultaFormulario.html', {'formulario': formulario})


############ PROFESIONALES ############

def profesionales(request):
    return render(request, "AppCoder/profesional.html", {'profesionales': Profesionales.objects.all()})

def profesionales_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        formulario = ProfesionalesForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        Profesionales.objects.create(nombre =data['nombre'], nombreDeProfesional=data['nombreDeProfesional'], turno=data['turno']) 
        return redirect('Profesionales')    
    else:
        formulario = ProfesionalesForm()
    return render(request, "AppCoder/consultaFormulario.html", {'formulario': formulario}) 

def profesionales_delete (request, id_prof):
     profesionales = Profesionales.objects.get(id=id_prof)
     profesionales.delete()
    
     return redirect('Profesionales')

def profesionales_update(request, id_profesional):
    profesionales = Profesionales.objects.get(id=id_profesional)
    
    if request.method == 'POST':
         formulario = ProfesionalesForm(request.POST)

         if formulario.is_valid():
             data = formulario.cleaned_data
             profesionales.nombre = data ['nombre']
             profesionales.nombreDeProfesional = data ['nombreDeProfesional']
             profesionales.turno = data ['turno']
            
             profesionales.save()
            
             return redirect ('Profesionales')
    else:
         formulario = ProfesionalesForm(model_to_dict(profesionales))
    return render (request, 'AppCoder/consultaFormulario.html', {'formulario': formulario})
        
##### CONSULTA ########


@login_required
def consulta(request):
 return render(request, "AppCoder/consulta.html", {'consulta': Consulta.objects.all()})
    
       
def consulta_formulario (request): #se usan las mismas variables que en el forms 
    if request.method == 'POST':
        formulario = ConsultaForm(request.POST) # agrega esto y saca nombre post etc a los 37.15 de la clase 21
        # nombre = request.POST['nombre']
        # servicio = request.POST['servicio']
        # mail = request.POST['mail']
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Consulta.objects.create(nombre =data['nombre'], servicio=data['servicio'], mail=data['mail']) # a los 39.17 de la clase 21 cambia (nombre=nombre, servicio=servicio, mail=mail) 
        return redirect('Consultas')    
    else:
        formulario = ConsultaForm()
    return render(request, "AppCoder/consultaFormulario.html", {'formulario': formulario}) #agrega {formulario} a los 41.20 clase21


def consulta_delete (request, id_consul):
    consulta = Consulta.objects.get(id=id_consul)
    consulta.delete()
    
    return redirect('Consultas')

def consulta_update(request, id_consul):
    consulta = Consulta.objects.get(id=id_consul)
    
    if request.method == 'POST':
         formulario = ConsultaForm(request.POST)

         if formulario.is_valid():
             data = formulario.cleaned_data
             consulta.nombre = data ['nombre']
             consulta.servicio = data ['servicio']
             consulta.mail = data ['mail']
            
             consulta.save()
            
             return redirect ('Consulta')
    else:
        formulario = ConsultaForm(model_to_dict(servicios))
    return render(request, 'AppCoder/consultaFormulario.html', {'formulario': formulario})





################## BUSQUEDA ############

#clase 21 a los 1.18 crea esta funcion
def busqueda_consulta(request):
    return render(request, "AppCoder/busquedaConsulta.html")

#clase 21 a los 1.25 crea esta funcion
def buscar(request):
    nombre = request.GET["nombre"]
    
    if request.GET['nombre']:
        servicio= Consulta.objects.filter(nombre=nombre)
    
        return render(request, "AppCoder/buscar.html",
        {'servicios' : servicio,'nombre' : nombre})
    else:
        return HttpResponse('No es valido')
    
    
    
    # return HttpResponse(f'Estoy buscando la consulta de: {request.GET["nombre"]}') #el nombre lo saca del template busquedaConsulta en el body esta declarada la variable de busqueda

###################################################################################

#estas tiene que ser la nuevas views, FALTA CREAR SUS HTML#


# class AvatarView:
#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             contexto['avatar_url'] = Avatar.objects.filter(user=self.request.user).last().imagen.url
#         return contexto

# #SERVICIOS#
# class ServiciosListView(LoginRequiredMixin, AvatarView, ListView):
#     model =  Servicios
#     template_name = "AppCoder/servicio.html"
#     context_object_name = 'servicio'

# class ServicioaDetailView(DetailView):
#     model=  Servicios
#     template_name= "AppCoder/servicios_ver.html"
    
# class  ServiciosCreateView(AvatarView, CreateView):
#     model=  Servicios
#     success_url= reverse_lazy('servicio')
#     Fields =['nombre', 'servicio', 'detalleDeServicio' ]
#     template_name = 'AppCoder/servicios_form.html'
        
# class  ServiciosUpdateView(UpdateView):
#     model=  Servicios
#     success_url= reverse_lazy('servicio')
#     Fields =['nombre', 'servicio', 'detalleDeServicio' ]
#     template_name = 'AppCoder/servicios_form.html'
    
# class ServiciosDeleteView(DeleteView):
#     model=  Servicios
#     success_url= reverse_lazy('servicio')
#     # template_name toma por default 'AppCoder/profesor_confirm_delete.html'
# #
    
    
# #PROFESIONALES#
# class ProfesionalesListView(LoginRequiredMixin, AvatarView, ListView):
#     model =  Profesionales
#     template_name = "AppCoder/profesional.html"
#     context_object_name = 'profesionales'

# class ProfesionalesDetailView(DetailView):
#     model=  Profesionales
#     template_name= "AppCoder/profesionales_ver.html"
    
# class  ProfesionalesCreateView(AvatarView, CreateView):
#     model=  Profesionales
#     success_url= reverse_lazy('profesionales')
#     Fields =['nombre', 'nombreDeProfesional', 'turno' ]
#     template_name = 'AppCoder/profesional_form.html'
        
# class  ProfesionalesUpdateView(UpdateView):
#     model=  Profesionales
#     success_url= reverse_lazy('profesionales')
#     Fields =['nombre', 'nombreDeProfesional', 'turno' ]
#     template_name = 'AppCoder/profesional_form.html'
    
# class ProfesionalDeleteView(DeleteView):
#     model=  Profesionales
#     success_url= reverse_lazy('profesionales')
#     # template_name toma por default 'AppCoder/profesor_confirm_delete.html'
    
    
# #CONSULTAS#
# class ConsultaListView(LoginRequiredMixin, AvatarView, ListView):
#     model =  Consulta
#     template_name = "AppCoder/consulta.html"
#     context_object_name = 'consulta'

# class ConsultaDetailView(DetailView):
#     model=  Consulta
#     template_name= "AppCoder/consulta_ver.html"
    
# class  ConsultaCreateView(AvatarView, CreateView):
#     model=  Consulta
#     success_url= reverse_lazy('Consulta')
#     Fields =['nombre', 'servicio', 'email' ]
#     template_name = 'AppCoder/consulta_form.html'
        
# class  ConsultaUpdateView(UpdateView):
#     model=  Consulta
#     success_url= reverse_lazy('Consulta')
#     Fields =['nombre', 'servicio', 'email' ]
#     template_name = 'AppCoder/consulta_form.html'
    
# class ConsultaDeleteView(DeleteView):
#     model=  Consulta
#     success_url= reverse_lazy('consulta')
#     # template_name toma por default 'AppCoder/profesor_confirm_delete.html'
    
    

def nosotros (request):
    return render(request, "AppCoder/nosotros.html")

