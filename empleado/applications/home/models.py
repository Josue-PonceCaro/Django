from statistics import mode
from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtile = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' - ' + self.subtile + ' - ' + str(self.cantidad) 