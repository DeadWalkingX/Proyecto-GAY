from django.db import models

# Create your models here.
class Paciente(models.Model):
    rut = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)    
    nombre = models.CharField(max_length=100)
    fechanac = models.DateField()
    telefono = models.IntegerField()
    telefonoEmergencias = models.IntegerField()
    direccion = models.CharField(max_length=100)
    observacion = models.CharField(max_length=1500,default = "Observacion")
    estado = models.CharField(max_length= 100, default= "Leve")

class Medico(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()    
    archivo = models.FileField(upload_to='archivos/Medico/')
    especialidad = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

class MedicoPostulante(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()    
    archivo = models.FileField(upload_to='archivos/Postulante/')
    especialidad = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

class Repartidor(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    celular = models.IntegerField()
    correo = models.CharField(max_length=100)
    
    