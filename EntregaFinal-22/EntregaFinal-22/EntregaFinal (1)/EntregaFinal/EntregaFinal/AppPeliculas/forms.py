from django import forms

class TerrorFormulario(forms.Form):
    mas_vistas = forms.CharField(max_length=40)
    taquilla = forms.IntegerField()
    critica_peliculas = forms.CharField(max_length=40)
    
class AccionFormulario(forms.Form):
    mas_vistas = forms.CharField(max_length=40)
    taquilla = forms.IntegerField()
    critica_peliculas = forms.CharField(max_length=40)
    
class AventuraFormulario(forms.Form):
    mas_vistas = forms.CharField(max_length=40)
    taquilla = forms.IntegerField()
    critica_peliculas = forms.CharField(max_length=40)
    