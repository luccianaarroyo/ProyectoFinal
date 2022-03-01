from pyexpat import model
from django.forms import model_to_dict
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.urls import reverse_lazy  

from AppCoder.forms import ServiciosForm, ProfesionalesForm, ConsultaForm, AvatarFormulario
from AppCoder.models import Servicios, Profesionales, Consulta, Avatar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

def inicio(request):
    #---- AVATAR ROMPE NO RECONOSE OBJETS ---- 
    avatares = Avatar.objects.filter()

    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''

    return render(request, 'AppCoder/inicio.html', {'avatar_url': avatar_url})
   
#NUEVA VIEW AVATAR RESUMIDO
class AvatarView:
      def get_context_data(self, **kwargs):
          contexto = super().get_context_data(**kwargs)
          if self.request.user.is_authenticated:
              contexto['avatar_url'] = Avatar.objects.filter(user=self.request.user).last().imagen.url
          return contexto

##### CONSULTA ######################################################################################################################
# @login_required
# def consulta(request):
#  return render(request, "AppCoder/consulta.html", {'consulta': Consulta.objects.all()})
    
       
# def consulta_formulario (request): #se usan las mismas variables que en el forms 
#     if request.method == 'POST':
#         formulario = ConsultaForm(request.POST) # agrega esto y saca nombre post etc a los 37.15 de la clase 21
    
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             Consulta.objects.create(nombre =data['nombre'], servicio=data['servicio'], mail=data['mail']) # a los 39.17 de la clase 21 cambia (nombre=nombre, servicio=servicio, mail=mail) 
#         return redirect('consultas')    
#     else:
#         formulario = ConsultaForm()
#     return render(request, "AppCoder/consultaFormulario.html", {'formulario': formulario}) #agrega {formulario} a los 41.20 clase21

#EN CONSULTA NO HACE FLTA EL UPDATE Y DELETE#
# def consulta_delete (request, id_consul):
#     consulta = Consulta.objects.get(id=id_consul)
#     consulta.delete()
    
#     return redirect('Consultas')

# def consulta_update(request, id_consul):
#     consulta = Consulta.objects.get(id=id_consul)
    
#     if request.method == 'POST':
#          formulario = ConsultaForm(request.POST)

#          if formulario.is_valid():
#              data = formulario.cleaned_data
#              consulta.nombre = data ['nombre']
#              consulta.servicio = data ['servicio']
#              consulta.mail = data ['mail']
            
#              consulta.save()
            
#              return redirect ('Consulta')
#     else:
#         formulario = ConsultaForm(model_to_dict(servicios))
#     return render(request, 'AppCoder/consultaFormulario.html', {'formulario': formulario})


# NUEVAS VIEWS DE CONSULTAS  NO HACE FALTA #################################################

class ConsultaListView(LoginRequiredMixin, AvatarView, ListView):
     model =  Consulta
     template_name = "AppCoder/consulta.html"
     context_object_name = 'consultas'
     
class ConsultaDetailView(DetailView):
     model=  Consulta
     template_name= "AppCoder/consulta_ver.html"
    
class  ConsultaCreateView(AvatarView, CreateView):
     model=  Consulta
     success_url= reverse_lazy('consultas')
     fields = '__all__'
     template_name = 'AppCoder/consulta_form.html'
        
class  ConsultaUpdateView(UpdateView):
     model=  Consulta
     success_url= reverse_lazy('consultas')
     fields =['nombre', 'servicio', 'email' ]
     template_name = 'AppCoder/consulta_form.html'
    
class ConsultaDeleteView(DeleteView):
     model=  Consulta
     success_url= reverse_lazy('consultas')
     #template_name='AppCoder/profesor_confirm_delete.html'

################## BUSQUEDA ######################################################################################

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


############ SERVICIOS #########################################################################################
# REEMPLAZADO POR ServiciosListView###########################################
def servicios(request):
    return render(request, "AppCoder/servicios.html", {'Servicios': Servicios.objects.all()})


# REEMPLAZADO POR ServiciosCreateView###########################################
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


# REEMPLAZADO POR ServiciosDeleteView###########################################
def servicios_delete (request, id_servi):
    servicios = Servicios.objects.get(id=id_servi)
    servicios.delete()
    
    return redirect('Servicios')


# REEMPLAZADO POR serviciosUpdateView###########################################
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

# NUEVAS VIEWS DE SERVICIOS####################################################################################
class ServiciosListView(AvatarView, ListView):
     model =  Servicios
     template_name = "AppCoder/servicios.html"
     context_object_name = 'servicios'
    
class  ServiciosCreateView(CreateView):
     model=  Servicios
     success_url= reverse_lazy('servicios')
     fields =['nombre', 'servicio', 'detalleDeServicio' ]
     template_name = 'AppCoder/servicios_form.html'
        
class  ServiciosUpdateView(UpdateView):
     model=  Servicios
     success_url= reverse_lazy('servicios')
     fields =['nombre', 'servicio', 'detalleDeServicio' ]
     template_name = 'AppCoder/servicios_form.html'
    
class ServiciosDeleteView(DeleteView):
     model=  Servicios
     success_url= reverse_lazy('servicios')
     #template_name= 'AppCoder/servicios_confirm_delete.html'

class ServiciosDetailView(DetailView):
     model=  Servicios
     template_name= "AppCoder/servicios_ver.html"


############ PROFESIONALES reemplazado por nuevas views#####################################################################################
#REEMPLAZADO POR  ListView#
# def profesionales(request):

#     return render(request, "AppCoder/profesional.html", {'profesionales': Profesionales.objects.all()})


# ##REEMPLAZADO POR  ProfesionalesCreateView####################################
# def profesionales_formulario (request): #se usan las mismas variables que en el forms 

#     if request.method == 'POST':
#         formulario = ProfesionalesForm(request.POST)
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
#         Profesionales.objects.create(nombre =data['nombre'], nombreDeProfesional=data['nombreDeProfesional'], turno=data['turno']) 
#         return redirect('Profesionales')    
#     else:
#         formulario = ProfesionalesForm()
#     return render(request, "AppCoder/consultaFormulario.html", {'formulario': formulario}) 


# # REEMPLAZADO POR ProfesionalesDeleteView###########################################
# def profesionales_delete (request, id_prof):
#      profesionales = Profesionales.objects.get(id=id_prof)
#      profesionales.delete()
    
#      return redirect('Profesionales')


# # REEMPLAZADO POR ProfesionalesUpDteView###########################################
# def profesionales_update(request, id_profesional): 
#     profesionales = Profesionales.objects.get(id=id_profesional)
    
#     if request.method == 'POST':
#          formulario = ProfesionalesForm(request.POST)

#          if formulario.is_valid():
#              data = formulario.cleaned_data
#              profesionales.nombre = data ['nombre']
#              profesionales.nombreDeProfesional = data ['nombreDeProfesional']
#              profesionales.turno = data ['turno']
            
#              profesionales.save()
            
#              return redirect ('Profesionales')
#     else:
#          formulario = ProfesionalesForm(model_to_dict(profesionales))
#     return render (request, 'AppCoder/consultaFormulario.html', {'formulario': formulario})


# NUEVAS VIEWS DE PROFESIONALES#######################################################################
class ProfesionalesListView(AvatarView, ListView):
     model =  Profesionales
     template_name = "AppCoder/profesionales.html"
     context_object_name = 'profesionales'
     
class  ProfesionalesCreateView(CreateView):
     model=  Profesionales
     success_url= reverse_lazy('profesionales')
     fields = ['nombre', 'nombreDeProfesional', 'turno' ]
     template_name = 'AppCoder/profesionales_form.html'
        
class  ProfesionalesUpdateView(UpdateView):
     model=  Profesionales
     success_url= reverse_lazy('profesionales')
     fields =['nombre', 'nombreDeProfesional', 'turno' ]
     template_name = 'AppCoder/profesionales_form.html'
    
class ProfesionalesDeleteView(DeleteView):
     model=  Profesionales
     success_url= reverse_lazy('profesionales')
     #template_name= 'AppCoder/profesionales_confirm_delete.html'

class ProfesionalesDetailView(DetailView):
     model=  Profesionales
     template_name= "AppCoder/profesionales_ver.html"   
###################################################################################
    
def nosotros (request):
    return render(request, "AppCoder/nosotros.html")

@login_required()
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('Inicio')
    else:
        formulario = AvatarFormulario()

    return render(request, 'AppCoder/crear_avatar.html', {'form': formulario})
