# Generated by Django 2.1.2 on 2019-06-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medic', '0004_horalibre_horatomada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutPaciente', models.CharField(max_length=100)),
                ('hora', models.IntegerField()),
                ('fecha', models.CharField(max_length=100)),
                ('observacion', models.CharField(max_length=100)),
            ],
        ),
    ]
