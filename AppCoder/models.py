from django.db.models import Model
from django.db.models.fields import CharField, EmailField
from django.forms import IntegerField


class inicio(Model):
    menu = CharField(max_length=40)
    
class servicios(Model):
    Manicura = CharField(max_length=40)
    Masajes = CharField(max_length=40)
    Color_y_corte = CharField(max_length=40)
    Pestañas = CharField(max_length=40)
     
class profesionales(Model):
    Zoe = CharField(max_length=40)
    Aldana = CharField(max_length=40)
    Tamara = CharField(max_length=40)
    Mateo = CharField(max_length=40)
    Juan = CharField(max_length=40)
    Maria = CharField(max_length=40)
    
class Consulta(Model):
    nombre = CharField(max_length=40)
    servicio = CharField(max_length=40)
    mail = EmailField()
    # telefono = IntegerField() - modificado por sugerenccia de WP
    def __str__ (self) -> str: #formulario
        return f'Consulta ({self.nombre})({self.servicio})({self.mail})'
    
    