from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.forms import ServiciosForm, ProfesionalesForm, ConsultaForm
from AppCoder.models import Servicios, Profesionales, Consulta
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy1   #no lo importa

from AppCoder.models import Servicios, Profesionales, Consulta
from django.contrib.auth.decorators import login_required


def inicio(request):
    #---- AVATAR ROMPE NO RECONOSE OBJETS ---- 
    # avatar_url = Avatar.objects.filter(user= request.user)
    # if avatares:
    #     avatar_url = avatares.last().imagen.url
    # else:
    #     avatar_url = ''
    return render(request, "AppCoder/inicio.html") #, {'avatar_url' : avatar_url}

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

# def servicios_delete (request, id_servicio):
#     servicios = Servicios.objects.get(id=id_servicio)
#     servicios.delete()
    
#     return redirect('Servicios')

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

#def profesionales_delete (request, id_profesional):
#     profesionales = Profesionales.objects.get(id=id_profesional)
#     profesionales.delete()
    
#     return redirect('Profesionales')

#def profesionales_update(request, id_profesional):
    # profesionales = Profesionales.objects.get(id=id_profesional)
    
    # if request.method == 'POST':
    #     data = ProfesionalesForm(request.POST)

    #     if formulario.is_valid():
    #         data = formulario.cleaned_data
    #         profesionales.nombre = data ['nombre']
    #         profesionales.nombreDeProfesional = data ['nombreDeProfesional']
    #         profesionales.turno = data ['turno']
            
    #         profesionales.save()
            
    #         return redirect ('Profesionales')
    # else:
    #     formulario = ProfesionalesForm(model_to_dict(profesionales))
    # return render (request,  )
        
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


# def consulta_delete (request, id_consulta):
#     consulta = Consulta.objects.get(id=id_consulta)
#     consulta.delete()
    
#     return redirect('Consultas')



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

#estas tiene que ser la nuevas views#

class ServiciosListView(ListView):
    model = Servicios
    template_name = "AppCoder/servicio.html"


class ServiciosDetailView(DetailView):
    model= Servicios
    template_name= "AppCoder/servicio_ver.html" #c
    
class ServiciosCreateView(CreateView):
    model= Servicios
    success_url= "AppCoder/servicio.html"
    Fields =['nombre', 'servicio', 'detalleDeServicio' ]
    
class ServiciosUpdat1eView(UpdateView):
    model= Servicios
    success_url= "AppCoder/servicio.html"
    Fields =['nombre', 'servicio', 'detalleDeServicio' ]
    
class ServiciosDeleteView(DeleteView):
    model= Servicios
    success_url= "AppCoder/servicio_delete.html"



class ProfesionalessListView(ListView):
    model = Profesionales
    template_name = "AppCoder/profesional.html"


class ProfesionaleDetailView(DetailView):
    model= Profesionales
    template_name= "AppCoder/profesional_ver.html" #c
    
class ProfesionalesCreateView(CreateView):
    model= Profesionales
    #success_url=  reverse_lazy ('profesionales')   #por algun motivo reverse_lazy lo marca como error
    Fields =['nombre', 'nombreDeProfesional', 'turno' ]
    template_name = "AppCoder/profesional_form.html" 
    
class ProfesionalesUpdat1eView(UpdateView):
    model= Profesionales
    success_url= "AppCoder/profesional.html"
    Fields =['nombre', 'nombreDeProfesional', 'turno' ]
    
class ProfesionaleDeleteView(DeleteView):
    model= Profesionales
    success_url= "AppCoder/profesional_delete.html"
    
    
    
    
    
    
class ConsultaListView(ListView):
    model =  Consulta
    template_name = "AppCoder/consulta.html"
    #context_object_name = 'servicios'

class ConsultaDetailView(DetailView):
    model=  Consulta
    template_name= "AppCoder/consulta.html" #c
    
class  ConsultaCreateView(CreateView):
    model=  Consulta
    success_url= "AppCoder/consulta.html"
    Fields =['nombre', 'servicio', 'email' ]
    
class  ConsultaUpdateView(UpdateView):
    model=  Consulta
    success_url= "AppCoder/consulta.html"
    Fields =['nombre', 'servicio', 'email' ]
    
class ConsultaDeleteView(DeleteView):
    model=  Consulta
    success_url= "AppCoder/consulta.html"
    
    
    

def nosotros (request):
    return render(request, "AppCoder/nosotros.html")