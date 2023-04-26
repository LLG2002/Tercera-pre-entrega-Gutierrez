
from inicio.models import Clientes
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect

class ListaClientes(ListView):
    model = Clientes
    template_name = 'inicio/lista_clientes_cbv.html'
    
class CrearUsuario(CreateView):
    model = Clientes
    fields=['usuario', 'contraseña', 'email', 'telefono']
    template_name ='inicio/crear_usuario_cbv.html'
    success_url = '/clientes/'
    
    
class EditarUsuario(UpdateView):
    model = Clientes
    fields = ['usuario', 'contraseña', 'email', 'telefono']
    template_name ='inicio/editar_cbv.html'
    success_url = '/clientes/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

class EliminarUsuario(DeleteView):
    model = Clientes
    template_name = 'inicio/eliminar_usuario_cbv.html'
    succes_url = '/clientes/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context
    
    def get_success_url(self):
        return reverse('inicio_principal:inicio')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

class MostrarUsuario(DetailView):
    model = Clientes
    template_name = 'inicio/mostrar_usuario_cbv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

