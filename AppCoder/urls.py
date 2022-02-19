
from AppCoder.views import inicio, servicios, profesionales, consulta,consulta_formulario,busqueda_consulta,buscar
from django.urls import path


urlpatterns = [
    
    
    path('', inicio, name="Inicio"),
    path("servicios", servicios,name="Servicios"),
    path("profesionales/", profesionales,name="Profesionales"),
    path("consultas", consulta,name="Consultas"),
    path('consultaFormulario', consulta_formulario, name='consulta_formulario'),
    path('busquedaConsulta', busqueda_consulta, name='busqueda_consulta'), # clase 21 a los 1.19 
    path('buscar', buscar, name='buscar'), # clase 21 a los 1.22

]
