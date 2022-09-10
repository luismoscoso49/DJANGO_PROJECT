from django.db import models

# Create your models here.

from django.db import models

class Medicos(models.Model):
    id_medico    = models.BigIntegerField(primary_key=True)
    nombre       = models.CharField(max_length=100)
    direccion    = models.CharField(max_length=100)
    telefono     = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100)

class Historia_Clinica(models.Model):
    id           = models.AutoField(primary_key=True)
id_paciente  = models.IntegerField()
id_medico    = models.ForeignKey(Medicos, on_delete=models.CASCADE)
fecha        = models.DateField()  
observaciones = models.CharField(max_length=200)
recomendaciones = models.CharField(max_length=400)

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


