from django import forms
from django.forms import Form, CharField, IntegerField #agregado clase 21 34:48
class ConsultaForm(forms.Form):
    nombre = forms.CharField()
    servicio = forms.CharField()
    mail = forms.EmailField() 
    