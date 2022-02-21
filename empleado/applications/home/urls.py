from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.pruebaView.as_view()),
    path('lista/',views.PruebaListView.as_view()),
    path('listaPrueba/',views.ListaPrueba.as_view()),
    path('create/',views.PruebaCreateView.as_view(), name = 'prueba_create'),
    path('prueba-fundation', views.ResumenFoundationView.as_view(), name = 'resumen fundation')
]
