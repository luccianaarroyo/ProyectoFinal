from django import forms
from django.forms import Form, CharField, IntegerField #agregado clase 21 34:48

class ServiciosForm(forms.Form):
    nombre = forms.CharField()
    servicio = forms.CharField()
    detalleDeServicio = forms.CharField() 
    
class ProfesionalesForm(forms.Form):
    nombre = forms.CharField()
    nombreDeProfesional = forms.CharField()
    turno = forms.CharField() 
    
class ConsultaForm(forms.Form):
    nombre = forms.CharField()
    servicio = forms.CharField()
    mail = forms.EmailField() 
    