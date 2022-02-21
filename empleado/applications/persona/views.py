from dataclasses import fields
from re import template
from django.shortcuts import render


from django.views.generic import (ListView, 
                                DetailView,
                                 CreateView,
                                  TemplateView,
                                   UpdateView,
                                   DeleteView,)

from applications.departamento.models import Departamento

from .models import Empleado, Habilidades

from django.urls import reverse_lazy 

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    ## paginate se usa para no pedir muchos datos de la base de datos,
    ## y asi no se pesado pedir tanta informacion
    ## add /?page=2 para ir en cada pagina << reto, hacer que la pagina pase haciendo click en un boton
    paginate_by = 4
    ordering = 'first_name'
    # model = Empleado
    def get_queryset(self):
        name = self.request.GET.get('fname','')
        
        lista = Empleado.objects.filter(
            first_name__icontains = name
        )
        return lista
        
    
class ListByArea(ListView):
    '''Lista empleados por area'''
    template_name = 'empleado/list_by_area.html'
    # queryset = Empleado.objects.filter(  # DO NOT DO QUERY'S LIKE THAT
    #     departamento__name = 'Software'
    # )
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__short_name = 'Ingenieria'
        # job = '3'
        # first_name = 'Jual'
        # departamento__name = 'Software'
        # habilidades__habilidad = 'Redactar'
    )
        return lista
    # context_object_name = 'lista'

class ListByName(ListView):
    template_name = 'empleado/list_by_name.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        nameKey = self.request.GET.get('fname','')
        lista = Empleado.objects.filter(
            first_name__icontains = nameKey
        )
        return lista
# Create your views here.
class ListByHabilidades(ListView):
    template_name = 'empleado/list_by_habilidades.html'
    model = Empleado
    def get_queryset(self):
        fname = self.request.GET.get('fname')
        lname = self.request.GET.get('lname')
        idN = self.request.GET.get('idN')
        print(idN)
        print(fname)
        print(lname)
        if idN:
            empleado = Empleado.objects.get(id=idN)
            
        elif fname:
            empleado = Empleado.objects.get(first_name = fname)
            
        elif lname:
            empleado = Empleado.objects.get(last_name = lname)
            
        else:
            empleado = Empleado.objects.get(id=1)
        habilidades = empleado.habilidades.all()
        return habilidades


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/empleado_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes' 
        return context
    

class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    # fields = '__all__' # TO GET ALL filds
    # success_url = '.' # To call the same page
    # success_url = '/success' # Not a good practice
    success_url = reverse_lazy('persona_app:all_ok')
    def form_valid(self, form):
        empleado = form.save(commit = False) # Just to instance, not to save, because then we will save
        empleado.full_name = empleado.first_name +' '+ empleado.last_name
        empleado.hoja_vida = 'Complete this now....'
        empleado.save()# save into the data base
        print(empleado)
        return super().form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:all_ok')

    def post(self, request, *args, **kwargs):
        print('\\\\\\\\\\\\\\POST')
        print(request.POST)
        print(request.POST['last_name'])
        print('0-------')
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        print('==------------------FORM VALID')
        return super().form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('persona_app:all_ok')


class HomeView(TemplateView):
    template_name = "inicio.html"
