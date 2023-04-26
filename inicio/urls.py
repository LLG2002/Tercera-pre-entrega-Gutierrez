from django.urls import path
from inicio import views

app_name= 'inicio_principal'
urlpatterns = [
    
    path('', views.CrearUsuario.as_view(), name='inicio'),
    path('clientes/', views.ListaClientes.as_view(), name='lista_clientes'),
    path('clientes/editar/<int:pk>/', views.EditarUsuario.as_view(), name='editar_usuario'),
    path('clientes/eliminar/<int:pk>/', views.EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('clientes/mostrar/<int:pk>/', views.MostrarUsuario.as_view(), name='mostrar_usuario'),
    
]