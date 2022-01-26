from django import forms

class ConsultaForm(forms.Form):
    nombre = forms.CharField()
    servicio = forms.CharField()
    mail = forms.EmailField() 
    telefono = forms.IntegerField()