from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, PasswordInput

class UserRegisterForm(UserCreationForm):
    
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        help_texts = {k: '' for k in fields}

#------------ 1 SI HABILITO ESTO ROMPE TODOO!!!! -------------        
# class UserEditForm(UserCreationForm):
#     email = EmailField(label='modificar email')
#     password1 = CharField(label='Contraseña', widget=PasswordInput)
#     password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)
#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2']
#         help_texts = {k: '' for k in fields}