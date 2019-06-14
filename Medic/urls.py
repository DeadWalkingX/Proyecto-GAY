from django.urls import path, include
from . import views

from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    #Link de navegacion
    path('', views.index, name="index"), 
    path('registro/', views.registro, name="registro"),
    path('informacion/', views.listadoPac, name="informacion"),
    path('observacion/', views.observacion, name="observacion"),
    path('mantenedor/', views.mantenedor, name="mantenedor"),
    path('asignarHorarios/', views.defHora, name="tomarHorarios" ),

    path('ex/', views.exp, name ="ex"),


    #Links para CRUD
    #Paciente
    path('registro/agregar_pac',views.crear_pac ,name="agregar_pac"),
    path('mantenedor/editar_pac/<int:id_pac>', views.editar_pac, name="editar_pac" ),
    path('mantenedor/eliminar_pac/<int:id_pac>', views.eliminar_pac, name="eliminar_pac" ),

    #Medico
    path('registro/agregar_med',views.crear_med ,name="agregar_med"),

    #Medico Postulante
    path('registro/agregar_med',views.crear_med_pos ,name="agregar_med_pos"),

    #Repartidor
    path('registro/agregar_rep',views.crear_rep ,name="agregar_rep"),
    path('mantenedor/editar_rep/<int:id_rep>', views.editar_rep, name="editar_rep" ),
    path('mantenedor/eliminar_rep/<int:id_rep>', views.eliminar_rep, name="eliminarr_rep" ),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
