from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        #Campos que el usuario puede editar
        fields = ['title', 'content', 'order']
        #Como es un formulario extendido, se puede agregar  los widgets para mejorar el formulario
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Contenido'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Order'}),
        }
        #Labels
        labels = {
            'title': '',
            'content': '',
            'order': '',
        }