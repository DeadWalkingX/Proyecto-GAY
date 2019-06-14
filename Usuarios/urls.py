from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required



app_name = 'Usuarios'

urlpatterns = [
    path('log/',views.login_page, name='log'),
    path('login/', views.login_iniciar , name='iniciar'),
    path('logout/', views.logout, name='logout'),
    path('login/', include('django.contrib.auth.urls')),
]