from django import forms
from .models import Categoria, Clubes

class UsuarioFormulario(forms.Form):
    Nombre_Usuario = forms.CharField(max_length=120)
    Email = forms.EmailField()
    Hincha = forms.CharField()
    Contraseña = forms.CharField()
    
class ClubesFormulario(forms.Form):

    Nombre = forms.CharField ()
    Ciudad = forms.CharField ()
    Provincia = forms.CharField()
    Categoria = forms.CharField()
    
    #Categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    
   # Nombre = forms.CharField ()
   # Ciudad = forms.CharField ()
   # Provincia = forms.CharField()
   # Categoria = forms.CharField()