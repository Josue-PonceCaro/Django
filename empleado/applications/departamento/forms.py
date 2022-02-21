from socket import fromshare
from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length = 50)
    apellidos = forms.CharField(max_length=50)
    departament = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=50)