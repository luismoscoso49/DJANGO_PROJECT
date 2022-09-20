#from asyncio.windows_events import NULL
from ctypes.wintypes import CHAR
import json
#from tkinter.tix import INTEGER
from unicodedata import numeric
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.db.models import Q
from datetime import datetime

from .models import Medicos
from .models import Pacientes 
from .models import Historia_Clinica
from .models import pacienteMedicoRel
from .models import Signos_Vitales
from .models import Historia_Signos
# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")    

### MEDICOS
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
        lista = []
        for reg in medico:
            data = {"medico" :reg.id_medico,"paciente" :reg.id_paciente}
            paciente = Pacientes.objects.filter(id_paciente = data["paciente"].id_paciente).filter()
            for xx in paciente:
                data = {"id_paciente": xx.id_paciente, "nombre" : xx.nombre}
                lista.append(data)
        
        medico = Medicos.objects.filter(id_medico=nid_medico).first()
        data = {
            "id_medico"		: medico.id_medico,		
            "nombre"		: medico.nombre,		
            "pacientes"		: lista
        }        
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    # except:
       #     return HttpResponse("Operacion no se pudo realizar")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def newHistoriaClinica(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            paciente = Pacientes (id_paciente = data["id_paciente"])
            medico   = Medicos (id_medico = data["id_medico"])

            historia = Historia_Clinica (
                    id_paciente=paciente,
                    id_medico=medico,
                    fecha=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                    observaciones=data["observaciones"],
                    recomendaciones=data["recomendaciones"],
                )
            historia.save()
            return HttpResponse("Apertura de Historia Clinica Exitosa ")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def updateHistoriaClinica(request, nid_paciente):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            medico = Medicos (id_medico = data["id_medico"],)

            historia = Historia_Clinica.objects.filter(id_paciente=nid_paciente).filter(id_medico = medico).first()
            if (not historia):
                return HttpResponseBadRequest("No existe una Historia Clinica para ese paciente y medico.")

            historia.fecha = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            historia.observaciones=data["observaciones"]
            historia.recomendaciones=data["recomendaciones"]

            historia.save()
            return HttpResponse("Historia Clinica Actualizada Satisfactoriamente")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deleteHistoriaClinica(request, nid_paciente, nid_medico):
    if request.method == 'DELETE':
        try:
            historia = Historia_Clinica.objects.filter(id_paciente=nid_paciente).filter(id_medico = nid_medico).all()
            if (not historia):
                return HttpResponseBadRequest("No existe un paciente con esa cédula.")

            historia.delete()
            return HttpResponse("Historia Clinica de Paciente eliminada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

#### PACIENTES
def newPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paciente = Pacientes(
                id_paciente=data["id_paciente"],
                nombre=data["nombre"],
                direccion=data["direccion"],
                telefono=data["telefono"],
            )
            paciente.save()
            return HttpResponse("Nuevo paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo No Valido")


def updatePaciente(request, nid_paciente):
    if request.method == 'PUT':
        try:
            paciente = Pacientes.objects.filter(id_paciente= nid_paciente).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe ese Paciente.")
            bandera = 0
            data = json.loads(request.body)
            try:
                paciente.nombre	=data["nombre"]
            except:
                bandera=0
            
            try:
                paciente.direccion=data["direccion"]
            except:
                bandera = 0

            try:
                paciente.telefono=data["telefono"]
            except:
                bandera = 0

            paciente.save()

            return HttpResponse("El proceso de Actualizacion de Pacientes termino satisfactoriamente")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deletePaciente(request, nid_paciente):
    if request.method == 'DELETE':
        try:
            paciente = Pacientes.objects.filter(id_paciente = nid_paciente).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe esa cuenta.")

            paciente.delete()
            return HttpResponse("Paciente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")


def getAllPacientes(request):
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()
        if (not pacientes):
            return HttpResponseBadRequest("No hay pacientes en la base de datos.")

        allPacientes = []
        for reg in pacientes:
            data = {
                "id_paciente": reg.id_paciente,
                "nombre": reg.nombre,
                "direccion": reg.direccion,
                "telefono": reg.telefono
            }

            allPacientes.append(data)
        dataJson = json.dumps(allPacientes)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def getPaciente(request, nid_paciente):
    if request.method == 'GET':
        paciente = Pacientes.objects.filter(id_paciente=nid_paciente).first()
        if (not paciente):
            return HttpResponseBadRequest("No existe un Paciente con esa cédula.")

        data = {
            "id_paciente":paciente.id_paciente,
            "nombre":paciente.nombre,
            "direccion":paciente.direccion,
            "telefono":paciente.telefono
        }

        dataJson = json.dumps(data)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

### SIGNOS VITALES
def newSignoVital(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            signos = Signos_Vitales(
                id_signo     = data["id_signo"],
                descripcion  = data["descripcion"],
                valor_minimo = data["valor_minimo"],
                valor_maximo = data["valor_maximo"],
                recomendacion =data["recomendacion"],
            )
            signos.save()
            return HttpResponse("Nuevo signo agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo No Valido")


def updateSignoVital(request, codSigno):
    if request.method == 'PUT':
        try:
            signo = Signos_Vitales.objects.filter(id_signo=codSigno).first()
            if (not signo):
                return HttpResponseBadRequest("No existe ese Signo Vital.")
            bandera = 0
            data = json.loads(request.body)
            try:
                signo.descripcion = data["descripcion"]
            except:
                bandera = 0

            try:
                signo.valor_minimo = data["valor_minimo"]
            except:
                bandera = 0

            try:
                signo.valor_maximo = data["valor_maximo"]
            except:
                bandera = 0

            try:
                signo.recomendacion = data["recomendacion"]
            except:
                bandera = 0

            signo.save()

            return HttpResponse("El proceso de Actualizacion de Signos Vitales termino satisfactoriamente")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteSignoVital(request, codSigno):
    if request.method == 'DELETE':
        try:
            signo = Signos_Vitales.objects.filter(id_signo=codSigno).first()
            if (not signo):
                return HttpResponseBadRequest("No existe ese Signo Vital.")

            signo.delete()
            return HttpResponse("Signo Vital eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")


def getAllSignos(request):
    if request.method == 'GET':
        signos = Signos_Vitales.objects.all()
        if (not signos):
            return HttpResponseBadRequest("No hay Signos Vitales en la base de datos.")

        allSignos = []
        for reg in signos:
            data = {
                "id_signo": reg.id_signo,
                "descripcion": reg.descripcion,
                "valor_minimo": str(reg.valor_minimo),
                "valor_maximo": str(reg.valor_maximo),
                "recomendacion": reg.recomendacion
            }
            allSignos.append(data)
        dataJson = json.dumps(allSignos)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def getSigno(request, codSigno):
    if request.method == 'GET':
        signo = Signos_Vitales.objects.filter(id_signo=codSigno).first()
        if (not signo):
            return HttpResponseBadRequest("No existe ese Signo Vital.")

        data = {
            "id_signo": signo.id_signo,
            "descripcion": signo.descripcion,
            "valor_minimo": str(signo.valor_minimo),
            "valor_maximo": str(signo.valor_maximo),
            "recomendacion": signo.recomendacion
        }

        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

## Historico Signos Vitales
def newHistoriaSignos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
 
            paciente = Pacientes (
                id_paciente=data["id_paciente"],
            )
            
            signos = Signos_Vitales(
                id_signo=data["id_signo"],
            )

            historia = Historia_Signos(
                id_paciente = paciente,
                id_signo=signos,
                fecha=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                valor_signo=data["valor_signo"],
            )

            historia.save()

            return HttpResponse("Nuevo reporte de signos agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo No Valido")


def updateHistoriaSignos(request, nid_paciente):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            signo = Signos_Vitales (id_signo = data["id_signo"],)

            historia = Historia_Signos.objects.filter(id_paciente=nid_paciente).filter(id_signo = signo).first()
            if (not historia):
                return HttpResponseBadRequest("No existe una Toma de Signos para ese paciente y Signos Vital.")

            historia.fecha = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            historia.valor_signo = data["valor_signo"]

            historia.save()
            return HttpResponse("Registro de Toma de Signos Vitales Actualizado Satisfactoriamente")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteHistoriaSignos(request, nid_paciente, codSigno):
    if request.method == 'DELETE':
        try:
            historia = Historia_Signos.objects.filter(
                id_paciente=nid_paciente).filter(id_signo=codSigno).all()
            if (not historia):
                return HttpResponseBadRequest("No existe un paciente con esa cédula.")

            historia.delete()
            return HttpResponse("Historia Clinica de Paciente eliminada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")
