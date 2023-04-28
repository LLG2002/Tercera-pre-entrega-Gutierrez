from django.urls import path
from inicio import views
from django.contrib.auth.views import LogoutView

app_name= 'inicio_principal'
urlpatterns = [
    
    path('inicio/', views.CrearUsuario.as_view(), name='inicio'),
    path('inicio/clientes/', views.ListaClientes.as_view(), name='lista_clientes'),
    path('inicio/clientes/editar/<int:pk>/', views.EditarUsuario.as_view(), name='editar_usuario'),
    path('inicio/clientes/eliminar/<int:pk>/', views.EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('inicio/clientes/mostrar/<int:pk>/', views.MostrarUsuario.as_view(), name='mostrar_usuario'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='inicio/logout.html'), name='logout'),
    path('', views.registrarse, name='registrarse'),   
]