from django.urls import path
from . import views

app_name="app"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.ListaPaciente.as_view(),name='lista'),
    path('crear', views.CrearPaciente.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
    path('login/', views.login, name='login'),
    path('<int:run>/lista_examen', views.ListaExamen.as_view(), name='lista_examen'),
    path('agregar', views.AgregarExamen.as_view(), name='agregar'),
   
]