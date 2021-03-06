from django.db import models

# Create your models here.

class Paciente(models.Model):
    run = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.run

class Examen(models.Model):
    run = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    resultado = models.CharField(max_length=50)

    def __str__(self):
        return self.run

class Medicamentos(models.Model):
    run = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.run