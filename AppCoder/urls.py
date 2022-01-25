from django.urls import path
from AppCoder.views import sucursal, servicio, profesional, turno, cliente

urlpatterns = [
    path("sucursal", sucursal),
    path("servicio", servicio),
    path("profesional", profesional),
    path("turno", turno),
    path("cliente", cliente),
]
