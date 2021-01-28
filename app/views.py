
from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from .models import Paciente
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 


# Create your views here.

def inicio(request):
    return render (request, 'app/index.html')


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