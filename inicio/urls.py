from django.urls import path
from inicio import views

app_name= 'inicio_principal'
urlpatterns = [
    
    path('', views.CrearUsuario.as_view(), name='inicio'),
    path('clientes/', views.ListaClientes.as_view(), name='lista_clientes'),
    path('<int:pk>/editar/', views.EditarUsuario.as_view(), name='editar_usuario'),
    path('<int:pk>/eliminar/', views.EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('<int:pk>/mostrar/', views.MostrarUsuario.as_view(), name='mostrar_usuario'),
    
]