# Generated by Django 2.1.2 on 2019-06-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medic', '0003_auto_20190508_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='observacion',
            field=models.CharField(default='Observacion', max_length=1500),
        ),
    ]