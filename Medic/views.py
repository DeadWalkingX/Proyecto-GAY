from django.shortcuts import render, redirect
from .models import Paciente, Medico, Repartidor, MedicoPostulante
from Usuarios.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


# Link a otras paginas
def index(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')

def exp(request):
    return render(request,'horariosM.html')

def defHora(request):
    return render(request, 'asignarHorarios.html')

def listadoPac(request):
    pacientes = Paciente.objects.all()
    contexto = {'pacientes':pacientes}
    return render(request,"pacientes.html",contexto)

def observacion(request):
    return render(request,"observacion.html")   

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
    lista = Paciente.objects.all()
    for p in lista:
        if(p.correo == correo):
            return HttpResponse('<script>alert("Ya hay alguien registrado con ese correo electronico."); window.location.href="/";</script>')
    pac = Paciente(rut=rut, correo=correo, nombre=nombre, fechanac=fechanac,
     telefono=telefono, telefonoEmergencias=telefonoEmergencias, direccion=direccion)
    pac.save()
    user = User.objects.create_user(email=correo, password=contra, tipo='pac', rut=rut)
    user.save()
    return redirect('Usuarios:log')

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

def eliminar_pac(request, id_pac):
    p = Paciente.objects.get(id=id_pac)
    p.delete()
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
    lista = Medico.objects.all()
    for m in lista:
        if(m.correo == correo):
            return HttpResponse('<script>alert("Ya hay alguien registrado con ese correo electronico."); window.location.href="/";</script>')
    med = Medico(rut=rut, nombre=nombre, telefono=telefono, contrasenia=contra, 
     archivo=archivo, especialidad=especialidad, correo=correo)
    med.save()    
    user = User.objects.create_user(email=correo,password=contra, tipo='med', rut = rut)
    user.save()
    return redirect('mantenedor')

#CRUD Medicos Postulantes
def crear_med_pos(request):
    correo = request.POST.get('correo')
    contra = request.POST.get('contra')
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')    
    telefono = request.POST.get('telefono')
    archivo = request.Files.get('archivo')
    especialidad = request.POST.get('especialidad')
    lista = MedicoPostulante.objects.all()
    for mp in lista:
        if(mp.correo == correo):
            return HttpResponse('<script>alert("Ya hay alguien registrado con ese correo electronico."); window.location.href="/";</script>')
    med = MedicoPostulante(rut=rut, nombre=nombre, telefono=telefono, contrasenia=contra, 
     archivo=archivo, especialidad=especialidad, correo=correo)
    med.save() 
    return redirect('Usuarios:log')

#CRUD Repartidores
def crear_rep(request):
    correo = request.POST.get('correo')
    contra = request.POST.get('contra')
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')    
    telefono = request.POST.get('telefono')   
    lista = Repartidor.objects.all()
    for r in lista:
        if(r.correo == correo):
            return HttpResponse('<script>alert("Ya hay alguien registrado con ese correo electronico."); window.location.href="/";</script>')
    rep = Repartidor(rut=rut, nombre=nombre, celular=telefono, correo=correo)
    rep.save()    
    user = User.objects.create_user(email=correo,password=contra,tipo='rep', rut = rut)
    user.save()
    return redirect('Usuarios:log')

def editar_rep(request, id_rep):
    r = Repartidor.objects.get(id=id_rep)
    nombre = request.POST.get('nombre') 
    rut = request.POST.get('rut')
    correo = request.POST.get('correo')
    telefono = request.POST.get('telefono') 
    r.nombre = nombre
    r.rut = rut 
    r.correo = correo
    r.telefono = telefono
    r.save()
    return redirect('mantenedor')

def eliminar_rep(request, id_rep):
    r = Repartidor.objects.get(id=id_rep)
    r.delete()
    return redirect('mantenedor')

#Crud Horas 
@login_required
def crear_horaLibre(request):
    inicio = request.POST.get('ini')
    fin = request.POST.get('fin')
    for i in range(inicio,fin):
        hl = HoraLibre(rutMedico= )


