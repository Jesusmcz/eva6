

from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from .models import Paciente, Examen
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages 


# Create your views here.

def inicio(request):
    return render (request, 'app/index.html')


def login(request):
    return render (request, 'app/panel.html')


class ListaPaciente(ListView):
    model=Paciente
    template_name = 'app/lista_paciente.html'
    context_object_name = 'paciente'


class CrearPaciente(CreateView):
    model=Paciente
    template_name = 'app/crear_paciente.html'
    fields='__all__'
    success_url= reverse_lazy('app:lista')


class EditarPaciente(UpdateView):
    model=Paciente
    template_name = 'app/editar_paciente.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista')


class EliminarPaciente(DeleteView):
    model=Paciente
    template_name = 'app/eliminar_paciente.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista')
    context_object_name = 'paciente'


class ListaExamen(ListView):
    model=Examen
    template_name = 'app/lista_examen.html'
    context_object_name = 'examen'


class AgregarExamen(CreateView):
    model=Examen
    template_name='app/agregar_examen.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista_examen')



""" class EliminarExamen(DeleteView):
    model=Examen
    template_name='app/eliminar_examen.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista_examen')
    context_object_name='examen' """

