
from django.views.generic.base import View
from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from .models import Paciente, Examen, Medicamentos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages 


# Create your views here.

def inicio(request):
    return render (request, 'app/index.html')


class Inicio(LoginRequiredMixin, View):
    def get (self, request):
        return render (request, 'app/panel.html')


class ListaPaciente(ListView):
    model=Paciente
    template_name = 'app/lista_paciente.html'
    context_object_name = 'paciente'

lista=[]
class PacientePersonalizado(View):
    def get(self, request, pk):
        resultado=list(Examen.objects.values().all())
        for elemento in resultado:
            resultado = elemento.get('resultado')
            lista.append(resultado)
        lista_paciente =list(Paciente.objects.filter(run=pk).values())
        context = {'paciente': lista_paciente, 'run':pk, 'lista':lista}
        return render(request, 'app/paciente_per.html', context=context)

""" def usuario(usuario):
    if usuario.profile.rol == 'Usuarios':
        validacion = True
    else:
        validacion = False
    return validacion    """

class CrearPaciente(LoginRequiredMixin, CreateView):
    model=Paciente
    template_name = 'app/crear_paciente.html'
    fields='__all__'
    success_url= reverse_lazy('app:lista')
    login_url='app:login'
""" 
    def test_func(self):
        return usuario(self.request.user) """


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


class ListaMedicamentos(ListView):
    model=Medicamentos
    template_name = 'app/lista_med.html'
    context_object_name = 'medicamento'


class AgregarMedicamentos(CreateView):
    model=Medicamentos
    template_name = 'app/agregar_med.html'
    fields='__all__'
    success_url= reverse_lazy('app:lista_med')


class EliminarMedicamento(DeleteView):
    model=Medicamentos
    template_name = 'app/eliminar_med.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista_med')
    context_object_name = 'medicamento'

class EditarMedicamento(UpdateView):
    model=Medicamentos
    template_name = 'app/editar_med.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista_med')





""" class EliminarExamen(DeleteView):
    model=Examen
    template_name='app/eliminar_examen.html'
    fields='__all__'
    success_url=reverse_lazy('app:lista_examen')
    context_object_name='examen' """

