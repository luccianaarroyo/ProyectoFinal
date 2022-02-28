from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, EmailField, TextField, DateField
from django.forms import IntegerField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField  
class inicio(Model):
    menu = CharField(max_length=40)
    
class Servicios(Model):
    nombre = CharField(max_length=40)
    servicio = CharField(max_length=40)
    detalleDeServicio = CharField(max_length=40)
    
    def __str__ (self) -> str: #formulario
        return f'servicios ({self.nombre})({self.servicio})({self.detalleDeServicio})'
    
     
class Profesionales(Model):
    nombre = CharField(max_length=40)
    nombreDeProfesional = CharField(max_length=40)
    turno = CharField(max_length=40)  #turno tarde o turno mañana
    
    def __str__ (self) -> str: #formulario
        return f'profesionales ({self.nombre})({self.nombreDeProfesional})({self.turno})'
    
    
class Consulta(Model):
    nombre = CharField(max_length=40)
    servicio = CharField(max_length=40)
    mail = EmailField()
    # telefono = IntegerField() - modificado por sugerenccia de WP
    def __str__ (self) -> str: #formulario
        return f'Consulta ({self.nombre})({self.servicio})({self.mail})'
    

# def get_image_filename(instance, filename):
#     title =  'titulo'
#     slug = slugify(title)
#     return "imagenesAvatares/%s-%s" % (slug, filename)  

class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)



def __str__(self):       
    return f"Imagen de: {self.user.username}"

class Post(Model):
    titulo = CharField('Titulo', max_length= 1000, blank=True, null=True)
    descripcion = CharField('Descripcion', max_length= 1000, blank=True, null=True)
    contenido = RichTextField()
    fecha_creacion = DateField('Fecha de Creacion', auto_now=False, auto_now_add = True)