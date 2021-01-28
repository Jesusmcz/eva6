from django.urls import path
from . import views

app_name="app"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.ListaPaciente.as_view(),name='lista'),
    path('crear', views.CrearPaciente.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
]