
from django.urls import path
from AppCoder.views import inicio, AvatarView, consulta, consulta_formulario, busqueda_consulta, buscar, nosotros, agregar_avatar, servicios, servicios_formulario, servicios_delete, servicios_update
from AppCoder.views import ServiciosListView, ServiciosCreateView, ServiciosUpdateView, ServiciosDeleteView, ServiciosDetailView, ProfesionalesListView, ProfesionalesCreateView, ProfesionalesUpdateView, ProfesionalesDeleteView, ProfesionalesDetailView #ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView, ConsultaDetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    
    path('', inicio, name="Inicio"),
    path('user/avatar/add', agregar_avatar, name="avatar_add"),
    #sin cambio - archivo Eli
    # path("servicios", servicios,name="Servicios"),
    # path('serviciosFormulario', servicios_formulario, name='servicios_formulario'),
    # path('profesionales', profesionales ,name='Profesionales'),
    # path('profesionalesFormulario', profesionales_formulario, name='profesionales_formulario'),
    # path("consultas", consulta,name="Consultas"),
    # path('consultaFormulario', consulta_formulario, name='consulta_formulario'), 
    # path('busquedaConsulta', busqueda_consulta, name='busqueda_consulta'), # clase 21 a los 1.19 
    # path('buscar', buscar, name='buscar'), # clase 21 a los 1.22
    # path('nosotros', nosotros, name='nosotros'),
    
     ##MANERA VIEJA Y LARGA#
    path('consulta', login_required(consulta), name='consultas'),
    path('consultaFormulario', consulta_formulario, name='consulta_formulario'),
    path('busquedaConsulta', busqueda_consulta, name='busqueda_consulta'),
    path('buscar', buscar, name='buscar'),
    
    path('busquedaConsulta', busqueda_consulta, name='busqueda_consulta'), # clase 21 a los 1.19 
    path('buscar', buscar, name='buscar'), # clase 21 a los 1.22
    path('nosotros', nosotros, name='nosotros'),
      
      
    ##CONSULTAS MANERA NUEVA Y RESUMIDA
    # path('consulta', ProfesionalesListView.as_view(), name='Consultas'),
    # path('consulta/add', ProfesionalesCreateView.as_view(), name='consulta_formulario'),
    # path('consulta/update/<pk>', ProfesionalesUpdateView.as_view(), name='consulta_update'),
    # path('consulta/delete/<pk>', ProfesionalesDeleteView.as_view(), name='consulta_delete'),
    #path('consulta/view/<pk>', ProfesionalesDetailView.as_view(), name='consulta_ver'),
    
    #MANERA NUEVA Y RESUMIDA#
    path('servicios', ServiciosListView.as_view(), name='servicios'),
    path('servicios/add', ServiciosCreateView.as_view(), name='servicios_formulario'),
    path('servicios/update/<pk>', ServiciosUpdateView.as_view(), name='servicios_update'),
    path('servicios/delete/<pk>', ServiciosDeleteView.as_view(), name='servicios_delete'),
    path('servicios/view/<pk>', ServiciosDetailView.as_view(), name='servicios_ver'),
    
     ##MANERA VIEJA Y LARGA#
    # path('servicios', servicios, name='servicios'),
    # path('serviciosFormulario', servicios_formulario, name='servicios_formulario'),
    # path('servicios/update/<pk>', servicios_update, name='servicios_update'),
    # path('servicios/delete/<pk>', servicios_delete, name='servicios_delete'),
    
    #MANERA NUEVA Y RESUMIDA#
    path('profesionales', ProfesionalesListView.as_view(), name='profesionales'),
    path('profesionales/add', ProfesionalesCreateView.as_view(), name='profesionales_formulario'),
    path('profesionales/update/<pk>', ProfesionalesUpdateView.as_view(), name='profesionaless_update'),
    path('profesionales/delete/<pk>', ProfesionalesDeleteView.as_view(), name='profesionales_delete'),
    path('profesionales/view/<pk>', ProfesionalesDetailView.as_view(), name='profesionales_ver'),
    
     ##MANERA VIEJA Y LARGA#
    #path('profesionales', profesionales, name='profesionales'),
    # path('profesionalesFormulario', profesionales_formulario, name='profesionales_formulario'),
    # path('profesionales/update/<pk>', profesionales_update, name='profesionales_update'),
    # path('profesionales/delete/<pk>', profesionales_delete, name='profesionales_delete')
    
]