from django.shortcuts import render, redirect
from django.template import Template, context, loader
from django.http import HttpResponse
from inicio.models import Clientes
from inicio.forms import CreacionClienteFormulario, BuscarCliente, EditarUsuario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# def inicio(request):
    
#     if request.method == "POST":
#         formulario = CreacionClienteFormulario(request.POST)
#         if formulario.is_valid():
#             datos_correctos = formulario.cleaned_data
#             cliente = Clientes(usuario=datos_correctos['usuario'], contraseña=datos_correctos['contraseña'], telefono=datos_correctos['telefono'], email=datos_correctos['email'])
#             cliente.save()
#             return redirect('/clientes')
#     else:
#         formulario = CreacionClienteFormulario()
#     return render(request, 'inicio/login.html', {'formulariocliente': formulario})


# def lista_clientes(request):
#      usuario_a_buscar= request.GET.get('usuario', None)
     
#      if usuario_a_buscar: 
#         clientes= Clientes.objects.filter(nombre__icontains=usuario_a_buscar)
#      else:
#         clientes= Clientes.objects.all()
     
#      formulario_busqueda= BuscarCliente()
#      return render(request, 'inicio/lista_clientes.html', {'usuario': clientes, 'formulario': formulario_busqueda}) 

# def editar_usuario(request, id_usuario):
#     usuario_a_editar = Clientes.objects.get(id=id_usuario)
    
#     if request.method == "POST":
#         formulario = EditarUsuario(request.POST)
#         if formulario.is_valid():
#             data_limpia = formulario.cleaned_data
            
#             usuario_a_editar.contraseña = data_limpia['contraseña']
#             usuario_a_editar.email = data_limpia['email']
#             usuario_a_editar.telefono = data_limpia['telefono']

#             usuario_a_editar.save()
            
#             return redirect('inicio_principal:lista_clientes')
#         else:
#             return render(request, 'inicio/editar_cbv.html', {'formulario': formulario, 'id_usuario': id_usuario})
#     else:
#         formulario = EditarUsuario(initial={'contraseña': usuario_a_editar.contraseña, 'email': usuario_a_editar.email, 'telefono': usuario_a_editar.telefono})
#         return render(request, 'inicio/editar_cbv.html', {'formulario': formulario, 'id_usuario': id_usuario})

class ListaClientes(ListView):
    model = Clientes
    template_name = 'inicio/lista_clientes_cbv.html'
    forms = BuscarCliente
    
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
    forms = EditarUsuario

class EliminarUsuario(DeleteView):
    model = Clientes
    template_name = 'inicio/eliminar_usuario_cbv.html'
    succes_url = 'inicio/lista_clientes_cbv.html'
    
class MostrarUsuario(DetailView):
    model = Clientes
    template_name = 'inicio/mostrar_usuario_cbv.html'