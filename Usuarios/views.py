from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.

#LOGIN



def login_page(request):
    return render(request,'login.html')

def login_iniciar(request):
    email = request.POST.get('correo')
    password = request.POST.get('contra')
    print(email,"  ",password)
    user = authenticate(request, email=email, password=password)
    print(email,"  ",password)
    if user is not None:
        login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/";</script>')

def logout_view(request):
    logout(request)
    return redirect('index')