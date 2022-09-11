from ctypes.wintypes import CHAR
import json
from tkinter.tix import INTEGER
from unicodedata import numeric
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.db.models import Q

from .models import Medicos
from .models import Pacientes 
from .models import Historia_Clinica
from .models import pacienteMedicoRel
# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")    

def newMedico(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            medico = Medicos(
                id_medico=data["id_medico"],
                nombre=data["nombre"],
                direccion=data["direccion"],
                telefono=data["telefono"],
                especialidad=data["especialidad"],
            )
            medico.save()
            return HttpResponse("El Medico " + data["nombre"] + " fue adicionada(o) ")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
       return HttpResponseNotAllowed(['POST'],'Metodo Invalido') 


def updateMedico(request, nid_medico):
    if request.method == 'PUT':
        try:
            medico = Medicos.objects.filter(id_medico=nid_medico).first()
            if (not medico):
                return HttpResponseBadRequest("No existe un medico con esa cédula.")
            data = json.loads(request.body)
            medico.nombre = data["nombre"]
            medico.direccion = data["direccion"]
            medico.telefono = data["telefono"]
            medico.especialidad = data["especialidad"]
            medico.save()
            return HttpResponse("Medico actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteMedico(request, nid_medico):
    if request.method == 'DELETE':
        try:
            medico = Medicos.objects.filter(id_medico=nid_medico).first()
            if (not medico):
                return HttpResponseBadRequest("No existe un medico con esa cédula.")

            medico.delete()
            return HttpResponse("Medico eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")


def getAllMedicos(request):
    if request.method == 'GET':
        medicos = Medicos.objects.all()
        if (not medicos):
            return HttpResponseBadRequest("No hay medicos en la base de datos.")
        allCustData = []
        for medico in medicos:
            data = {
                "id_medico": medico.id_medico,
                "nombre": medico.nombre,
                "direccion": medico.direccion, 
                "telefono": medico.telefono,
                "especialidad": medico.especialidad
                }
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getMedico(request, nid_medico):
    if request.method == 'GET':
        medico = Medicos.objects.filter(id_medico=nid_medico).first()
        if (not medico):
            return HttpResponseBadRequest("No existe un medico con esa cédula.")
        data = {
            "id_medico"		: medico.id_medico,		
            "nombre"		: medico.nombre,		
            "direccion"		: medico.direccion,
            "telefono"		: medico.telefono,		
            "especialidad"	: medico.especialidad
        }
        dataJson = json.dumps(data)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def pacientesxmedico(request, nid_medico):
    if request.method == 'GET':
        medico = pacienteMedicoRel.objects.filter(id_medico=nid_medico).all()
        if (not medico):
            return HttpResponseBadRequest("No existe un medico con esa cédula.")
        try:    
            lista = []
            for reg in medico:
                paciente = Pacientes.objects.filter(id_paciente = reg.id_paciente).filter()
                for xx in paciente:
                    data = {"nombre" : xx.nombre}
                    lista.append(data)
        
            medico = Medicos.objects.filter(id_medico=nid_medico).first()
            data = {
                "id_medico"		: medico.id_medico,		
                "nombre"		: medico.nombre,		
                "pacientes"		: lista
            }        
            dataJson = json.dumps(data)
            #print(dataJson)
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = dataJson
            return resp
        except:
            return HttpResponse("Operacion no se pudo realizar")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def newHistoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            historia = Historia_Clinica (
                    id_paciente=data["id_paciente"],
                    id_medico=data["id_medico"],
                    observaciones=data["observaciones"],
                    recomendaciones=data["recomendaciones"],
                )
            historia.save()
            return HttpResponse("Apertura de Historia Clinica Exitosa ")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def updateHistoria(request, nid_paciente):
    if request.method == 'PUT':
        try:
            paciente = Historia_Clinica.objects.filter(id_paciente=nid_paciente).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe un paciente con esa cédula.")
            data = json.loads(request.body)
            id_medico=data["id_medico"],
            observaciones=data["observaciones"],
            recomendaciones=data["recomendaciones"],
            paciente.save()
            return HttpResponse("Medico actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deleteHistoria(request, nid_paciente):
    if request.method == 'DELETE':
        try:
            paciente = Historia_Clinica.objects.filter(id_medico=nid_paciente).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe un paciente con esa cédula.")

            paciente.delete()
            return HttpResponse("Historia Clinica de Paciente eliminada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")
