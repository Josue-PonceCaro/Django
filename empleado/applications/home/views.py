from dataclasses import fields
from pipes import Template
from re import template
from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, ListView, CreateView)

from .models import Prueba
class pruebaView(TemplateView): 
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/list.html"
    queryset = ['0','1','10','20','30']
    context_object_name = 'ListaNumeros'
    
class ListaPrueba(ListView):
    template_name = 'home/list_prueba.html'
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields = ['titulo','subtile','cantidad']
