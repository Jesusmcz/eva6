from django.contrib import admin
from .models import Paciente, Examen
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Examen)