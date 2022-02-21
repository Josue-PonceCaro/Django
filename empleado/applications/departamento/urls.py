from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new-departament/', views.NewDepartamentoView.as_view(), name='NDepartamento'), 
]
