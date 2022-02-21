from operator import mod
from pyexpat import model
from tabnanny import verbose
from django.db import models
from applications.departamento.models import Departamento


from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = 'Habilidad de la persona'
        verbose_name_plural = 'Todas las habilidades'
        ordering = ['habilidad']
    def __str__(self):
        return str(self.id)+'-'+self.habilidad

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
    full_name = models.CharField(
        'Nombre Completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('trabajo',max_length=50, choices=job_choice)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    avatar = models.ImageField(upload_to = 'empleado', blank = True, null = True)
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Administrador de empleados'
        ordering = ['-id']

    def __str__(self) :
        return str(self.id) + ' - ' + self.first_name + '-' + self.last_name