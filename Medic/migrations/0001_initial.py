# Generated by Django 2.1.2 on 2019-06-13 23:09

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
                ('archivo', models.FileField(upload_to='archivos/Medico/')),
                ('especialidad', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('horaInicio', models.IntegerField()),
                ('horaFin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicoPostulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('archivo', models.FileField(upload_to='archivos/Postulante/')),
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
                ('nombre', models.CharField(max_length=100)),
                ('fechanac', models.DateField()),
                ('telefono', models.IntegerField()),
                ('telefonoEmergencias', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('observacion', models.CharField(default='Observacion', max_length=1500)),
                ('estado', models.CharField(default='Leve', max_length=100)),
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
            ],
        ),
    ]
