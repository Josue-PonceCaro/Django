from django.contrib import admin
from django.urls import path

def testerDepartamento(self):
    print('Testing departamento -----------------------------@@@@@@')

urlpatterns = [
    path('departamento/',testerDepartamento),
    
]
