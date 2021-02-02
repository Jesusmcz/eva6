from django.urls import path
from . import views

app_name="app"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.ListaPaciente.as_view(),name='lista'),
    path('crear', views.CrearPaciente.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
    path('panel/', views.Inicio.as_view(), name='login'),
    path('lista_examen', views.ListaExamen.as_view(), name='lista_examen'),
    path('agregar', views.AgregarExamen.as_view(), name='agregar'),
    path('lista_med', views.ListaMedicamentos.as_view(), name='lista_med'),
    path('agregar_med', views.AgregarMedicamentos.as_view(), name='agregar_med'),
    path('eliminar_med', views.EliminarMedicamento.as_view(), name='eliminar_med'),
    path('editar_med', views.EditarMedicamento.as_view(), name='editar_med'),
   
]