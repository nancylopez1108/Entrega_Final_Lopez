
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Medicos/', views.Medicos, name="Medicos"),
    path('Turnos/', views.turnos, name="Turnos"),
    path('Pacientes/', views.Pacientes, name="Pacientes"),
    path('turnosFormulario/', views.turnosFormulario, name="turnosFormulario"),
    path("pacientesFormulario/", views.pacientesFormulario, name="pacientesFormulario"),
    path("busquedaTurno/", views.busquedaTurno, name="busquedaTurno"),
    path("buscar/", views.buscar, name="buscar"),
    path("medicosFormulario/", views.medicosFormulario, name="medicosFormulario"),

]
