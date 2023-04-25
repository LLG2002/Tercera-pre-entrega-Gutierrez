
from inicio.models import Clientes
from inicio.forms import CreacionClienteFormulario, BuscarCliente, EditarUsuarioFormulario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django import forms

class BaseClientes(forms.Form):
    model = Clientes
    forms = CreacionClienteFormulario
    fields = ['usuario', 'contraseña', 'email', 'telefono']

class ListaClientes(ListView):
    model = Clientes
    template_name = 'inicio/lista_clientes_cbv.html'
    
class CrearUsuario(CreateView):
    model = Clientes
    forms = CreacionClienteFormulario
    fields = ['usuario', 'contraseña', 'email', 'telefono']
    template_name ='inicio/crear_usuario_cbv.html'
    success_url = '/clientes/'
    
    
class EditarUsuario(UpdateView):
    model = Clientes
    # forms = EditarUsuarioFormulario
    fields = ['usuario', 'contraseña', 'email', 'telefono']
    template_name ='inicio/editar_cbv.html'
    success_url = '/clientes/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

class EliminarUsuario(BaseClientes,DeleteView):
    model = Clientes
    template_name = 'inicio/eliminar_usuario_cbv.html'
    succes_url = '/clientes/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

class MostrarUsuario(BaseClientes,DetailView):
    model = Clientes
    template_name = 'inicio/mostrar_usuario_cbv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

