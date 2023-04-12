from django import forms

class CreacionClienteFormulario(forms.Form):
    usuario = forms.CharField(max_length=15)
    contraseña = forms.CharField(max_length=15)
    email= forms.CharField(max_length=25)
    edad= forms.IntegerField()

class BuscarCliente(forms.Form):
    usuario = forms.CharField(max_length=15, required=False)
    contraseña = forms.CharField(max_length=15, required=False)
    email= forms.CharField(max_length=25, required=False)
    edad= forms.IntegerField(required=False)