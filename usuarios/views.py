from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login


def registrarse(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
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
