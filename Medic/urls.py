from django.urls import path, include
from . import views

from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    #Link de navegacion
    path('', views.index, name="index"), 
    path('registro/', views.registro, name="registro"),
    path('login/', views.iniciar, name="login"),
    path('mantenedor/', views.mantenedor, name="mantenedor"),
    #Login
    path('login/in', views.login_iniciar, name="iniciar"),
    #Links para CRUD
    #Paciente
    path('registro/agregar_pac',views.crear_pac ,name="agregar_pac"),
    path('mantenedor/editar_pac/<int:id>', views.editar_pac, name="editar_pac" ),
    #Medico
    path('registro/agregar_med',views.crear_med ,name="agregar_med"),
    #Medico Postulante
    path('registro/agregar_med',views.crear_med_pos ,name="agregar_med_pos"),
    #Repartidor
    path('registro/agregar_rep',views.crear_rep ,name="agregar_rep"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
