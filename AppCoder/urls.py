from django.urls import path
from AppCoder.views import inicio, servicios, servicios_formulario, profesionales, profesionales_formulario,  consulta,consulta_formulario, nosotros, busqueda_consulta,buscar
from AppCoder.views import ServiciosListView, ServiciosCreateView, ServiciosUpdateView, ServiciosDeleteView, ServiciosDetailView, ProfesionalesListView, ProfesionalesCreateView, ProfesionalesUpdateView, ProfesionalesDeleteView, ProfesionalesDetailView, ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView, ConsultaDetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
#servicios_delete,
#profesionales_delete,
#consulta_delete,

urlpatterns = [  
    path('', inicio, name="Inicio"),
    
    path('busquedaConsulta', busqueda_consulta, name='busqueda_consulta'), # clase 21 a los 1.19 
    path('buscar', buscar, name='buscar'), # clase 21 a los 1.22
    path('nosotros', nosotros, name='nosotros'),
    
    path('servicios', ServiciosListView.as_view(), name='Servicios'),
    path('profesores/add', ServiciosCreateView.as_view(), name='servicios_formulario'),
    path('profesores/update/<pk>', ServiciosUpdateView.as_view(), name='servicios_update'),
    path('profesores/delete/<pk>', ServiciosDeleteView.as_view(), name='servicios_delete'),
    path('servicios/view/<pk>', ServiciosDetailView.as_view(), name='servicios_ver'),
    
    path('profesionales', ProfesionalesListView.as_view(), name='profesional'),
    path('profesionales/add', ProfesionalesCreateView.as_view(), name='profesionales_formulario'),
    path('profesionales/update/<pk>', ProfesionalesUpdateView.as_view(), name='profesionaless_update'),
    path('profesionales/delete/<pk>', ProfesionalesDeleteView.as_view(), name='profesionales_delete'),
    path('profesionales/view/<pk>', ProfesionalesDetailView.as_view(), name='profesionales_ver'),
    
    path('consulta', ConsultaListView.as_view(), name='Consulta'),
    path('profesionales/add', ConsultaCreateView.as_view(), name='consulta_formulario'),
    path('profesionales/update/<pk>', ConsultaUpdateView.as_view(), name='consulta_update'),
    path('profesionales/delete/<pk>', ConsultaDeleteView.as_view(), name='consulta_delete'),
    path('profesionales/view/<pk>', ConsultaDetailView.as_view(), name='consulta_ver'),
]
    
    
    #LAS NUEVAS URLS TIENE QUE SER ESTAS
    # path('profesionales/add', ProfesionalesCreateView.as_view(),name='profesionales_add'),
    # path('profesionales/update', ProfesionalesUpdateView.as_view(),name='profesionales_update'),
    # path('profesionales/delete', ProfesionalesDeleteView.as_view(),name='profesionales_delete'),
    # path('login', views.login_request, name = 'Login'),
    # path('register', views.register, name = 'Register'),
    # path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),
    # path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    #path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    
    
#url viejas#

    #path("servicios", servicios,name="Servicios"),
    #path('serviciosFormulario', servicios_formulario, name='servicios_formulario'),
    #path('servicios/delete/<id_servi>', servicios_delete, name='servicios_delete_servicio.id'),
    #path('servicios/update<id_servi>', servicios_delete, name='servicios_delete'),
    
    #path('profesionales', profesionales ,name='Profesionales'),
    #path('profesionalesFormulario', profesionales_formulario, name='profesionales_formulario'),
    #path('profesionales/delete/<id_prof>', profesionales_delete, name='profesionales_delete'),
    #path('profesionales/updatee/<id_prof>', profesionales_delete, name='profesionales_delete'),
    
    #path("consultas", consulta,name="Consultas"),
    #path('consultaFormulario', consulta_formulario, name='consulta_formulario'),
    #path('consulta/delete/<id_consul', consulta_delete, name='consulta_delete'),
    #path('consulta/delete/<id_consul>', consulta_delete, name='consulta_delete'),