from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtile = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    class Meta:
        verbose_name = 'Mi Pruebas'
        verbose_name_plural = 'Todas las pruebas' 
        ordering = ['titulo']  
        unique_together = ['titulo', 'subtile']     
    def __str__(self):
        return self.titulo + ' - ' + self.subtile + ' - ' + str(self.cantidad) 

