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
    path('perfil/',views.perfil, name="perfil"),


    #Links para CRUD
    #Paciente
    path('registro/agregar_pac',views.crear_pac ,name="agregar_pac"),
    path('mantenedor/editar_pac/<int:id_pac>', views.editar_pac, name="editar_pac" ),
    path('mantenedor/eliminar_pac/<int:id_pac>', views.eliminar_pac, name="eliminar_pac" ),

    #Medico
    path('mantenedor/agregar_med/<int:id_medpos>',views.crear_med ,name="agregar_med"),
    path('mantenedor/eliminar_medpos/<int:id_medpos>', views.eliminar_medpos, name="eliminar_medpos" ),

    #Medico Postulante
    path('registro/agregar_med_pos',views.crear_med_pos ,name="agregar_med_pos"),

    #Repartidor
    path('registro/agregar_rep',views.crear_rep ,name="agregar_rep"),
    path('mantenedor/editar_rep/<int:id_rep>', views.editar_rep, name="editar_rep" ),
    path('mantenedor/eliminar_rep/<int:id_rep>', views.eliminar_rep, name="eliminarr_rep" ),

    #Hora Libre
    path('perfil/crearHoras', views.crear_horaLibre, name="crearHoras"),
    path('perfil/eliminarHL', views.eliminar_horaLibre, name="eliminarHL"),

    #Hora Tomada
    path('perfil/crearHT/<int:rutMedico>/<int:hora>/<str:fecha>', views.crear_ht, name="crearHT"),
    path('perfil/eliminarHT', views.eliminar_horaTomada, name="eliminarHT"),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
