"""team14_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('newMedico', views.newMedico, name='newMedico'),
    path('updateMedico/<int:nid_medico>',
         views.updateMedico, name='updateMedico'),
    path('deleteMedico/<int:nid_medico>',
         views.deleteMedico, name='deleteMedico'),
    path('medicos', views.getAllMedicos, name='getAllMedicos'),
    path('getMedico/<int:nid_medico>', views.getMedico, name='getMedico'),
    path('pacientesxmedico/<int:nid_medico>', views.pacientesxmedico, name='pacientesxmedico'),
    path('newHistoria', views.newHistoria, name='newHistoria'),
    path('updateHistoria/<int:nid_paciente>',
         views.updateHistoria, name='updateHistoria'),
]

# http://127.0.0.1:8000/team14/index desde el browser

"""
urlpatterns = [
    path('home', views.home, name='Home'),
    path('newCustomer', views.newCustomer, name='newCustomer'),
    path('getAllCustomers', views.getAllCustomers, name='getAllCustomers'),
    path('getOneCustomer/<int:id>', views.getOneCustomer, name='getOneCustomer'),
]
"""
