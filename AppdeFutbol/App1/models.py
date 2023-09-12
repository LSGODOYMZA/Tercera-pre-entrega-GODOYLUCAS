from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    Nombre = models.CharField(max_length=100)
    Equipos = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.Nombre}'
    
    def clubes_asociados(self):
        return ", ".join([f"{club.Nombre} ({club.Ciudad})" for club in self.clubes.all()])

class Clubes(models.Model):
    Nombre = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    Provincia = models.CharField(max_length=100)
    Categoria = models.ForeignKey(Categoria, related_name='clubes', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('Nombre', 'Ciudad', 'Provincia')
    
    def __str__(self):
        return f'{self.Nombre}    (  {self.Ciudad}-{self.Provincia}  )'

class Usuario(models.Model):
    Nombre_Usuario = models.CharField(unique=True, max_length=120)
    Email = models.EmailField()
    Hincha = models.ForeignKey(Clubes, related_name='usuarios', on_delete=models.CASCADE)
    CrearContraseña = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.Nombre_Usuario}. Hincha de {self.Hincha}'