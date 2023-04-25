
from inicio.models import Clientes
from inicio.forms import CreacionClienteFormulario, BuscarCliente, EditarUsuarioFormulario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class ListaClientes(ListView):
    model = Clientes
    template_name = 'inicio/lista_clientes_cbv.html'
    forms = BuscarCliente
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario."] = self.get
        return context
    
class CrearUsuario(CreateView):
    model = Clientes
    template_name ='inicio/crear_usuario_cbv.html'
    success_url = '/clientes/'
    fields = ['usuario', 'contraseña', 'email', 'telefono']
    forms = CreacionClienteFormulario
    
class EditarUsuario(UpdateView):
    model = Clientes
    template_name ='inicio/editar_cbv.html'
    success_url = 'inicio/lista_clientes_cbv.html'
    fields = ['usuario', 'contraseña', 'email', 'telefono']
    forms = EditarUsuarioFormulario
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.post
        return context

class EliminarUsuario(DeleteView):
    model = Clientes
    template_name = 'inicio/eliminar_usuario_cbv.html'
    succes_url = 'inicio/lista_clientes_cbv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

class MostrarUsuario(DetailView):
    model = Clientes
    template_name = 'inicio/mostrar_usuario_cbv.html'