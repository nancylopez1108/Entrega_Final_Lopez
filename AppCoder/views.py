from django.http import HttpResponse
from django.shortcuts import render

from .models import Medico, Paciente, Turnos
from .forms import MedicosFormulario, PacientesFormulario, TurnosFormulario


def inicio(request):
    return render(request, "inicio.html")

def Pacientes(request):
    return render(request, "Pacientes.html")

def Medicos(request):
    lista_medicos = Medico.objects.all()
    return render(request, "Medicos.html", {"medicos": lista_medicos})

def turnos(request):
    return render(request, "Turnos.html")

def turnosFormulario(request):
    if request.method == "POST":
        miFormulario = TurnosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            turno = Turnos(
                nombre = informacion["nombre"],
                dni_paciente = informacion["dni_paciente"],
                fecha = informacion["fecha"],
                hora = informacion["hora"],
                especialidad = informacion["especialidad"] )
            turno.save()
            return render(request, "inicio.html")
    else:
        miFormulario = TurnosFormulario()

    return render(request, "turnosFormulario.html", {"miFormulario": miFormulario})




def pacientesFormulario(request):
    if request.method == "POST":
        miFormulario = PacientesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            paciente = Paciente( nombre=informacion["nombre"],apellido=informacion["apellido"],DNI=informacion["dni_paciente"],   
                email=informacion["email"])

            paciente.save()
            return render(request, "inicio.html")
    else:
        miFormulario = PacientesFormulario()
    return render(request, "pacientesFormulario.html", {"miFormulario": miFormulario})

def busquedaTurno(request):
    return render(request, "busquedaTurno.html")

def buscar(request):
    dni = request.GET.get("dni")

    if dni:
        turnos = Turnos.objects.filter(dni_paciente=dni)
        return render(request,"resultadosTurnos.html", {"turnos": turnos, "dni": dni})
    return HttpResponse("No enviaste DNI")

from django.shortcuts import render
from .forms import MedicosFormulario
from .models import Medico

def medicosFormulario(request):
    if request.method == "POST":
        miFormulario = MedicosFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            medico = Medico(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                especialidad=informacion["especialidad"],
                email=informacion["email"])
            medico.save()
            return render(request, "inicio.html")
    else:
        miFormulario = MedicosFormulario()

    return render(request, "medicosFormulario.html", {"miFormulario": miFormulario})


