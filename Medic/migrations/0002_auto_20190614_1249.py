# Generated by Django 2.1.2 on 2019-06-14 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='horaFin',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='horaInicio',
        ),
    ]