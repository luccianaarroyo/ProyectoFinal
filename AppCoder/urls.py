
from AppCoder.views import inicio, servicios, profesionales, consulta,consulta_formulario
from django.urls import path

urlpatterns = [

    path('', inicio, name="Inicio"),
    path("servicios", servicios,name="Servicios"),
    path("profesionales/", profesionales,name="Profesionales"),
    path("consultas", consulta,name="Consultas"),
    path('consultaFormulario', consulta_formulario, name='consulta_formulario'),

]
