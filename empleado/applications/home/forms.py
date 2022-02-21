from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Prueba
class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        # fields = "__all__"
        fields = ('titulo', 'subtile', 'cantidad')
        widgets = {
            'titulo' : forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese testo aqui'
                }
            )
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 5:
            raise forms.ValidationError('El cantidad %i es < que 5'%cantidad)
        return cantidad