from django import forms
from django.forms import Form, CharField, IntegerField, ImageField, EmailField, Textarea #agregado clase 21 34:48

from django.db.models.fields import (
    BooleanField, CharField, DateField, EmailField, IntegerField,
    GenericIPAddressField, URLField, DecimalField, TimeField
)
class ServiciosForm(Form):
#class ServiciosForm(forms.Form):
    nombre = forms.CharField()
    servicio = forms.CharField()
    detalleDeServicio = forms.CharField() 
    
class ProfesionalesForm(Form):
    nombre = forms.CharField(max_length=30)
    nombreDeProfesional = forms.CharField(max_length=30)
    turno = forms.CharField(max_length=30) 
    
class ConsultaForm(Form):
    nombre = CharField()
    servicio = CharField()
    mail = EmailField() 

class AvatarFormulario(Form):
    imagen = ImageField(required=True)

    

