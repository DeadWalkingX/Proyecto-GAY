# Generated by Django 2.1.2 on 2019-06-14 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Medic', '0002_auto_20190614_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicopostulante',
            name='contra',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
