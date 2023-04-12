from django.shortcuts import render, redirect
from django.template import Template, context, loader
from django.http import HttpResponse
from inicio.models import Clientes
from inicio.forms import CreacionClienteFormulario, BuscarCliente


def inicio(request):
    if request.method == "POST":
        formulario = CreacionClienteFormulario(request.POST)
        
        if formulario.is_valid(): 
            datos_correctos= formulario.cleaned_data
            
            cliente = Clientes(usuario= datos_correctos['usuario'], contraseña= datos_correctos['contraseña'], edad= datos_correctos['edad'], email= datos_correctos['email'] )
            cliente.save()
         
            return redirect('inicio:lista_clientes')
            
         
    formulario= CreacionClienteFormulario()
    return render(request, 'inicio/login.html', {'formulariocliente': formulario})

def lista_clientes(request):
     usuario_a_buscar= request.GET.get('usuario', None)
     
     if usuario_a_buscar: 
        clientes= Clientes.objects.filter(nombre__icontains=usuario_a_buscar)
     else:
        clientes= Clientes.objects.all()
     
     formulario_busqueda= BuscarCliente()
     return render(request, 'inicio/lista_clientes.html', {'usuario': clientes, 'formulario': formulario_busqueda}) 

