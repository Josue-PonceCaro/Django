from django.db import models
from applications.departamento.models import Departamento
# Create your models here.
class Empleado(models.Model):
    '''Modelo tabla empleados'''
    # TYPE OF JOB
    job_choice = (('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'OTRO'),)
        
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    job = models.CharField('trabajo',max_length=50, choices=job_choice)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.id) + ' - ' + self.first_name + '-' + self.last_name