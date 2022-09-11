# Generated by Django 4.1.1 on 2022-09-11 17:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team14App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia_clinica',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='id_medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team14App.medicos'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='id_paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team14App.pacientes'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='observaciones',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='recomendaciones',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='historia_signos',
            name='id_paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team14App.pacientes'),
        ),
        migrations.AddField(
            model_name='historia_signos',
            name='id_signo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team14App.signos_vitales'),
        ),
        migrations.AddField(
            model_name='historia_signos',
            name='valor_signo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='signos_vitales',
            name='descripcion',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='signos_vitales',
            name='recomendacion',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='signos_vitales',
            name='valor_maximo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='signos_vitales',
            name='valor_minimo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='historia_signos',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]