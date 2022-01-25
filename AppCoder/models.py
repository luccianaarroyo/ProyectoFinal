from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, EmailField

class Sucursal(Model):
    zona = CharField(max_length=40)
    
class Servicio(Model):
    Esculpidas = CharField(max_length=40)
    Kapping = CharField(max_length=40)
    Tintura = CharField(max_length=40)
    Corte = CharField(max_length=40)
    Peinado = CharField(max_length=40)
    
    
class Profesional(Model):
    Zoe = CharField(max_length=40)
    Aldana = CharField(max_length=40)
    Tamara = CharField(max_length=40)
    Mateo = CharField(max_length=40)
    Juan = CharField(max_length=40)
    
class Turno(Model):
    mes = CharField(max_length=40)
    dia = IntegerField()
    hora = IntegerField()
    
class Cliente(Model):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    mail = EmailField()