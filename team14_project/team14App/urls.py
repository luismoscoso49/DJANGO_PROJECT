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
    path('updateMedico/<int:nid_medico>',  views.updateMedico, name='updateMedico'),
    path('deleteMedico/<int:nid_medico>', views.deleteMedico, name='deleteMedico'),
    path('medicos', views.getAllMedicos, name='getAllMedicos'),
    path('getMedico/<int:nid_medico>', views.getMedico, name='getMedico'),
    path('pacientesxmedico/<int:nid_medico>', views.pacientesxmedico, name='pacientesxmedico'),
    path('newHistoriaClinica', views.newHistoriaClinica, name='newHistoriaClinica'),
    path('updateHistoriaClinica/<int:nid_paciente>',views.updateHistoriaClinica, name='updateHistoriaClinica'),
    path('deleteHistoriaClinica/<int:nid_paciente>/<int:nid_medico>',views.deleteHistoriaClinica, name='deleteHistoriaClinica'),
    path('newPaciente', views.newPaciente, name='newPaciente'),
    path('updatePaciente/<int:nid_paciente>',views.updatePaciente, name='updatePaciente'),
    path('deletePaciente/<int:nid_paciente>',views.deletePaciente, name='deletePaciente'),
    path('getAllPacientes', views.getAllPacientes, name='getAllPacientes'),
    path('getPaciente/<int:nid_paciente>', views.getPaciente, name='getPaciente'),
    path('newSignoVital', views.newSignoVital, name='newSignoVital'),
    path('updateSignoVital/<str:codSigno>',views.updateSignoVital, name='updateSignoVital'),
    path('deleteSignoVital/<str:codSigno>',views.deleteSignoVital, name='deleteSignoVital'),
    path('getAllSignos', views.getAllSignos, name='getAllSignos'),
    path('getSigno/<str:codSigno>', views.getSigno, name='getSigno'),
    path('newHistoriaSignos', views.newHistoriaSignos, name='newHistoriaSignos'),
    path('updateHistoriaSignos/<int:nid_paciente>',views.updateHistoriaSignos, name='updateHistoriaSignos'),
    path('deleteHistoriaSignos/<int:nid_paciente>/<str:codSigno>',views.deleteHistoriaSignos, name='deleteHistoriaSignos'),
]

# http://127.0.0.1:8000/team14/index desde el browser

