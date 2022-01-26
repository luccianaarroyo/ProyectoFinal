
from AppCoder.views import inicio, servicios, profesionales, consulta
from django.urls import path

urlpatterns = [
    path("inicio", inicio),
    path("servicios", servicios),
    path("profesionales", profesionales),
    path("consulta", consulta)
]
