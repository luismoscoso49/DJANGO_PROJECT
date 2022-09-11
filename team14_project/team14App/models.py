from tkinter import CASCADE
from django.db import models
from datetime import date

# Create your models here.

from django.db import models

#luis fernando 
class Pacientes (models.Model):
  id_paciente   = models.BigIntegerField(primary_key=True)
  nombre        = models.CharField(max_length=100)
  direccion     = models.CharField(max_length=100)
  telefono      = models.CharField(max_length=30)

class Medicos (models.Model):
    id_medico    = models.BigIntegerField(primary_key=True)
    nombre       = models.CharField(max_length=100)
    direccion    = models.CharField(max_length=100)
    telefono     = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100)

class pacienteMedicoRel (models.Model):
    id_paciente = models.ForeignKey(
        Pacientes, on_delete=models.CASCADE, blank=True, null=True)
    id_medico = models.ForeignKey(
        Medicos, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=['id_paciente', 'id_medico'], name='unique_migration_host_combination'
                )
            ]


class Historia_Clinica (models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, blank=True, null=True)
    id_medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateField(default=date.today)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    recomendaciones=models.CharField(max_length = 400, blank = True, null = True)

#Luis Orlando
class Signos_Vitales (models.Model):
    id_signo    = models.CharField(max_length=2, primary_key=True)
    descripcion =  models.CharField(max_length=50, default="N/A")
    valor_minimo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    valor_maximo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    recomendacion = models.CharField(max_length=100, default="N/A")

class Historia_Signos (models.Model):
    id          = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, blank = True, null = True)
    id_signo=models.ForeignKey(Signos_Vitales, on_delete = models.CASCADE, blank = True, null = True)
    fecha = models.DateField(default=date.today)
    valor_signo = models.DecimalField(max_digits=20, decimal_places=2, default=0)

"""
class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=False)

class Account(models.Model):
    number = models.IntegerField(primary_key=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    lastChangeDate = models.DateField()
    isActive = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, related_name='account', on_delete=models.CASCADE)

"""


