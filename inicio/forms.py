from django import forms

class CreacionClienteFormulario(forms.Form):
    usuario = forms.CharField(max_length=15)
    contraseña = forms.CharField(max_length=15)
    email= forms.CharField(max_length=25)
    telefono= forms.IntegerField()

class BuscarCliente(forms.Form):
    usuario = forms.CharField(max_length=15, required=False)
    contraseña = forms.CharField(max_length=15, required=False)
    email= forms.CharField(max_length=30, required=False)
    telefono= forms.IntegerField(required=False)
    
class EditarUsuarioFormulario(forms.Form):
    
    contraseña = forms.CharField(max_length=15, required=False)
    email= forms.CharField(max_length=30, required=False)
    telefono= forms.IntegerField(required=False)