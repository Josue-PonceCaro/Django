from ast import For
from re import template
from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
 
from applications.persona.models import Empleado

from .models import Departamento

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        departament = form.cleaned_data['departament']
        shortname = form.cleaned_data['shortname']
  
        depa = Departamento.objects.create(
            name=departament,
            short_name = shortname
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job ='1',
            departamento = depa
        )
        
        return super().form_valid(form)