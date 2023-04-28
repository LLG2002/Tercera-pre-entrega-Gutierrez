
from inicio.models import Clientes
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.mixins import LoginRequiredMixin

def registrarse(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio_principal:login')
        else:
            return render(request, 'inicio/registrar.html', {'formulario': formulario})
    
    formulario = UserCreationForm()
    return render(request, 'inicio/registrar.html', {'formulario': formulario})

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            return redirect('inicio_principal:inicio')
        else:
            return render(request, 'inicio/login.html', {'formulario': formulario})
            
        
    formulario = AuthenticationForm()
    return render(request, 'inicio/login.html', {'formulario': formulario})

class ListaClientes(ListView):
    model = Clientes
    template_name = 'inicio/lista_clientes_cbv.html'
    
class CrearUsuario(CreateView):
    model = Clientes
    fields=['usuario', 'conjunto', 'email', 'telefono', 'producto']
    template_name ='inicio/crear_usuario_cbv.html'
    success_url = '/clientes/'
    
    
class EditarUsuario(LoginRequiredMixin,UpdateView):
    model = Clientes
    fields = ['usuario', 'conjunto', 'email', 'telefono', 'producto']
    template_name ='inicio/editar_cbv.html'
    success_url = '/clientes/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

class EliminarUsuario(LoginRequiredMixin,DeleteView):
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

class MostrarUsuario(LoginRequiredMixin,DetailView):
    model = Clientes
    template_name = 'inicio/mostrar_usuario_cbv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.object
        return context

