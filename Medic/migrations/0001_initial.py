# Generated by Django 2.1.2 on 2019-05-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('contrasenia', models.CharField(max_length=100)),
                ('archivo', models.FileField(upload_to='archivos/')),
                ('especialidad', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('fechanac', models.DateField()),
                ('telefono', models.IntegerField()),
                ('telefonoEmergencias', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('celular', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=100)),
            ],
        ),
    ]