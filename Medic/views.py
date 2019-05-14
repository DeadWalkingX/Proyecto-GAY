from django.shortcuts import render, redirect
from .models import Paciente, Medico, Repartidor, MedicoPostulante
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.


# Link a otras paginas
def index(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')

def iniciar(request):
    return render(request,'login.html')

def mantenedor(request):
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    repartidores = Repartidor.objects.all()
    usuarios = User.objects.all()
    med_pos = MedicoPostulante.objects.all()
    contexto = {'pacientes':pacientes, 'medicos':medicos, 'repartidores':repartidores,'usuarios':usuarios, 'med_pos':med_pos}
    return render(request, 'mantenedor.html', contexto)


# CRUD Pacientes

def crear_pac(request):
    correo = request.POST.get('correo')
    contra = request.POST.get('contra')    
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')
    fechanac = request.POST.get('fechanac')
    telefono = request.POST.get('telefono')
    telefonoEmergencias = request.POST.get('telefono2')
    direccion = request.POST.get('direc')
    pac = Paciente(rut=rut, correo=correo, nombre=nombre, fechanac=fechanac,
     telefono=telefono, telefonoEmergencias=telefonoEmergencias, direccion=direccion)
    pac.save()
    user = User.objects.create_user(username=correo,email=correo,password=contra)
    user.save()
    return redirect('login')

def editar_pac(request, id_pac):
    paciente = Paciente.objects.get(pk=id_pac)
    correo = request.POST.get('correo')
    nombre = request.POST.get('nombre')
    telefono = request.POST.get('telefono')
    telefonoEmergencias = request.POST.get('telefono2')
    direccion = request.POST.get('direc')
    paciente.correo = correo
    paciente.nombre = nombre
    paciente.telefono = telefono
    paciente.telefonoEmergencias = telefonoEmergencias
    paciente.direccion = direccion
    return redirect('mantenedor')


#CRUD Medicos
def crear_med(request, id_med):
    agregado = MedicoPostulante.objects.get(pk=id_med)
    correo = agregado.correo
    contra = agregado.contra
    rut = agregado.rut
    nombre = agregado.nombre
    telefono = agregado.telefono
    archivo = agregado.archivo
    especialidad = agregado.especialidad
    med = Medico(rut=rut, nombre=nombre, telefono=telefono, contrasenia=contra, 
     archivo=archivo, especialidad=especialidad, correo=correo)
    med.save()    
    user = User.objects.create_user(username=correo,email=correo,password=contra)
    user.save()
    return redirect('login')

#CRUD Medicos Postulantes
def crear_med_pos(request):
    correo = request.POST.get('correo')
    contra = request.POST.get('contra')
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')    
    telefono = request.POST.get('telefono')
    archivo = request.Files.get('archivo')
    especialidad = request.POST.get('especialidad')
    med = Medico(rut=rut, nombre=nombre, telefono=telefono, contrasenia=contra, 
     archivo=archivo, especialidad=especialidad, correo=correo)
    med.save()    
    return redirect('login')

#CRUD Repartidores
def crear_rep(request):
    correo = request.POST.get('correo')
    contra = request.POST.get('contra')
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')    
    telefono = request.POST.get('telefono')   
    rep = Repartidor(rut=rut, nombre=nombre, celular=telefono, correo=correo)
    rep.save()
    user = User.objects.create_user(username=correo,email=correo,password=contra)
    user.save()
    return redirect('login')
