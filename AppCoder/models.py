from django.db.models import Model
from django.db.models.fields import CharField, EmailField
from django.forms import IntegerField


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
    


    