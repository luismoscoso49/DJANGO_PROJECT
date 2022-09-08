import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.db.models import Q

# from .models import Customer, Account
# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")    

def newMembers(request):
    if request.method == "POST":
       return HttpResponse("adicionando un nuevo miembro")
    else:
       return HttpResponseNotAllowed(['POST'],'Metodo Invalido') 

"""
def newCustomer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer = Customer(
                id = data["id"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                email = data["email"],
                password = data["password"],
            )
            customer.save()
            return HttpResponse("Nuevo cliente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllCustomers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        if (not customers):
            return HttpResponseBadRequest("No hay clientes en la base de datos.")

        allCustData = []
        for x in customers:
            data = {"id": x.id, "firstName": x.firstName, "lastName": x.lastName, "email": x.email}
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOneCustomer(request, id):
    if request.method == 'GET':
        customer = Customer.objects.filter(id = id).first()
        if (not customer):
            return HttpResponseBadRequest("No existe cliente con esa cédula.")

        data = {"id": customer.id, "firstName": customer.firstName, "lastName": customer.lastName, "email": customer.email}
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
"""	   

    
def getMembers(request):
    if request.method == "GET":
       return HttpResponse("CONSULTANDO UN miembro")
    else:
       return HttpResponseNotAllowed(['GET'],'Metodo Invalido')     