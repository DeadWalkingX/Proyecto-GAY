from django.shortcuts import render, redirect
from .models import Paciente, Medico, Repartidor, MedicoPostulante, HoraLibre, HoraTomada
from Usuarios.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime

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
    horalibre = HoraLibre.objects.all()
    horatomada = HoraTomada.objects.all()

    contexto = {'pacientes':pacientes, 'horaslibres':horalibre, 'medicos':medicos, 'repartidores':repartidores,'usuarios':usuarios, 'med_pos':med_pos, 'horaTomada':horatomada}
    return render(request, 'mantenedor.html', contexto)

def perfil(request):
        pacientes = Paciente.objects.all()
        medicos = Medico.objects.all()
        repartidores = Repartidor.objects.all()
        horalibre = HoraLibre.objects.all()
        horatomada = HoraTomada.objects.all()
        contexto = {'pacientes':pacientes,  'medicos':medicos, 'repartidores':repartidores, 'horalibre':horalibre, 'horatomada':horatomada}
        return render(request, 'perfil.html', contexto)

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
def crear_med(request, id_medpos):
    agregado = MedicoPostulante.objects.get(pk=id_medpos)
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
    med = Medico(rut=rut, nombre=nombre, telefono=telefono, 
     archivo=archivo, especialidad=especialidad, correo=correo)
    med.save()    
    user = User.objects.create_user(email=correo,password=contra, tipo='med', rut = rut)
    user.save()
    agregado.delete()
    return redirect('mantenedor')

#CRUD Medicos Postulantes
def crear_med_pos(request):
    correo = request.POST.get('correo')
    contra = request.POST.get('contra')
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')    
    telefono = request.POST.get('telefono')
    archivo = request.FILES.get('archivo')
    especialidad = request.POST.get('especialidad')
    lista = MedicoPostulante.objects.all()
    for mp in lista:
        if(mp.correo == correo):
            return HttpResponse('<script>alert("Ya hay alguien registrado con ese correo electronico."); window.location.href="/";</script>')
    med = MedicoPostulante(rut=rut, nombre=nombre, telefono=telefono, contra=contra, 
     archivo=archivo, especialidad=especialidad, correo=correo)
    med.save() 
    return HttpResponse('<script>alert("Se ha enviado su solicitud de registro. Debe esperar a que sea aceptado."); window.location.href="/";</script>')

def eliminar_medpos(request,id_medpos):
    r = MedicoPostulante.objects.get(id=id_medpos)
    r.delete()
    return redirect('mantenedor')

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

#Crud HorasLibres

@login_required
def crear_horaLibre(request):
    inicio = request.POST.get('inicio')
    fin = request.POST.get('fin')
    fecha = datetime.datetime.now()
    rut = request.user.rut
    mes = fecha.month
    ano = fecha.year
    aux = ""
    for i in range(fecha.day+1,fecha.day+3):
        aux = str(i) +'-' +str(mes) +'-' +str(ano)
        for j in range(int(inicio),int(fin)):
            hl = HoraLibre(rutMedico = rut, hora = j, fecha = aux)
            hl.save()

    return HttpResponse('<script>alert("Horas para los proximos dos dias creadas."); window.location.href="/";</script>')

@login_required
def eliminar_horaLibre(request):
        horaLibre = HoraLibre.objects.all()
        rut = request.user.rut
        for h in horaLibre:
                if (h.rutMedico == rut):
                        h.delete()
        return redirect('perfil')

def eliminar_horaTomada(request):
        horaTomada = HoraTomada.objects.all()
        rut = request.user.rut
        for ht in horaTomada:
                if (ht.rutMedico == rut):
                        ht.delete()
        return redirect('perfil')

#Crud Horas Tomadas

@login_required
def crear_ht(request,rutMedico,hora,fecha):
        horaslibres = HoraLibre.objects.all()
        for hl in horaslibres:
                print(hl.rutMedico,'=',rutMedico)
                print(hl.hora,'=',hora)
                print(hl.fecha,'=',fecha)
                if( int(hl.rutMedico) == rutMedico and int(hl.hora) == hora and str(hl.fecha) == fecha):

                        hl.delete()
                        ht = HoraTomada(rutMedico=rutMedico, rutPaciente=request.user.rut, hora=hora, fecha=fecha)
                        ht.save()
                        break
        
        return redirect('perfil')

        


