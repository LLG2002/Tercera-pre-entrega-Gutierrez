from django.urls import path
from inicio import views

app_name= 'inicio_principal'
urlpatterns = [
    path('', views.inicio, name='inicio'),
     path('clientes/', views.lista_clientes, name='lista_clientes'),
    
    
]