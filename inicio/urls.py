from django.urls import path
from inicio import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'inicio_principal'
urlpatterns = [
    
    path('inicio/', views.CrearUsuario.as_view(), name='inicio'),
    path('inicio/clientes/', views.ListaClientes.as_view(), name='lista_clientes'),
    path('inicio/clientes/editar/<int:pk>/', views.EditarUsuario.as_view(), name='editar_usuario'),
    path('inicio/clientes/eliminar/<int:pk>/', views.EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('inicio/clientes/mostrar/<int:pk>/', views.MostrarUsuario.as_view(), name='mostrar_usuario'),
    path('about/', views.about_me, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)